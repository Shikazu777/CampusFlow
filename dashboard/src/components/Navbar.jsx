import { FaBell } from "react-icons/fa";

function Navbar() {
  return (
    <div className="flex justify-between items-center mb-8">

      <div className="flex items-center gap-4">

        <div className="
          w-14
          h-14
          rounded-2xl
          bg-blue-600
          flex
          items-center
          justify-center
          text-2xl
          font-bold
        ">
          S
        </div>

        <div>
          <h2 className="text-2xl font-bold">
            SRM University
          </h2>

          <p className="text-slate-400">
            Campus Dashboard
          </p>
        </div>

      </div>

      <div className="flex items-center gap-6">

        <button className="
          p-4
          bg-slate-800
          rounded-2xl
          hover:bg-slate-700
          transition
        ">
          <FaBell size={20} />
        </button>

        <div className="flex items-center gap-3">

          <div>
            <h3 className="font-semibold">
              Dhanraj
            </h3>

            <p className="text-sm text-slate-400">
              Student
            </p>
          </div>

          <div className="
            w-12
            h-12
            rounded-full
            bg-blue-500
            flex
            items-center
            justify-center
            text-lg
            font-bold
          ">
            D
          </div>

        </div>

      </div>

    </div>
  );
}

export default Navbar;