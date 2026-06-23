import { useState } from "react";
import { useNavigate } from "react-router-dom";

import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";

import api from "../services/api";

function CreatePost() {

  const navigate = useNavigate();

  const [title, setTitle] =
    useState("");

  const [content, setContent] =
    useState("");

  async function handleSubmit(
    e
  ) {

    e.preventDefault();

    try {

      const userId =
        localStorage.getItem(
          "user_id"
        );

      await api.post(
        "/posts/",
        {
          user_id: Number(userId),
          title,
          content
        }
      );

      alert(
        "Post created"
      );

      navigate("/community");

    } catch (error) {

      console.log(error);

      alert(
        error.response?.data?.detail
        || "Failed to create post"
      );
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

        <h1 className="
          text-4xl
          font-bold
          mb-8
        ">
          Create Post
        </h1>

        <form
          onSubmit={handleSubmit}
          className="
            bg-slate-800
            p-8
            rounded-3xl
            max-w-3xl
          "
        >

          <input
            type="text"
            placeholder="Title"
            value={title}
            onChange={(e) =>
              setTitle(
                e.target.value
              )
            }
            className="
              w-full
              p-4
              rounded-2xl
              bg-slate-700
              mb-6
            "
          />

          <textarea
            placeholder="What's happening?"
            value={content}
            onChange={(e) =>
              setContent(
                e.target.value
              )
            }
            rows={8}
            className="
              w-full
              p-4
              rounded-2xl
              bg-slate-700
              mb-6
            "
          />

          <button
            className="
              bg-blue-600
              px-8
              py-4
              rounded-2xl
            "
          >
            Post
          </button>

        </form>

      </div>

    </div>
  );
}

export default CreatePost;