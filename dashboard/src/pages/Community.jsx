import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";

function Community() {
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

      </div>

    </div>
  );
}

export default Community;