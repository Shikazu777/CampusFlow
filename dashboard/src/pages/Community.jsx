import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";

import { getPosts } from "../services/communityService";

function Community() {

  const navigate = useNavigate();

  const [posts, setPosts] =
    useState([]);

  useEffect(() => {
    loadPosts();
  }, []);

  async function loadPosts() {

    try {

      const data =
        await getPosts();

      setPosts(data);

    } catch (error) {

      console.log(error);
    }
  }

  return (
    <div className="
      flex
      bg-slate-900
      min-h-screen
      text-white
    ">

      <Sidebar />

      <div className="flex-1 p-8">

        <Navbar />

        <div className="
          flex
          justify-between
          items-center
          mb-8
        ">

          <h1 className="
            text-4xl
            font-bold
          ">
            Community
          </h1>

          <button
            onClick={() =>
              navigate("/create-post")
            }
            className="
              bg-blue-600
              px-6
              py-3
              rounded-2xl
            "
          >
            Create Post
          </button>

        </div>

        <div className="space-y-6">

          {posts.map((post) => (

            <div
              key={post.id}
              className="
                bg-slate-800
                rounded-3xl
                p-6
              "
            >

              <h2 className="
                text-2xl
                font-bold
              ">
                {post.title}
              </h2>

              <p className="
                mt-4
                text-slate-300
              ">
                {post.content}
              </p>

              <div className="
                flex
                gap-8
                mt-6
              ">

                <span>
                  👍 {post.upvotes}
                </span>

                <span>
                  👎 {post.downvotes}
                </span>

              </div>

            </div>

          ))}

        </div>

      </div>

    </div>
  );
}

export default Community;