import {
  FaHome,
  FaUtensils,
  FaCalendarAlt,
  FaUsers,
  FaSearch,
  FaBell,
  FaChartBar,
  FaUser,
} from "react-icons/fa";

function Sidebar() {
  const menuItems = [
    { icon: <FaHome />, label: "Dashboard" },
    { icon: <FaUtensils />, label: "Food" },
    { icon: <FaCalendarAlt />, label: "Events" },
    { icon: <FaUsers />, label: "Community" },
    { icon: <FaSearch />, label: "Lost & Found" },
    { icon: <FaBell />, label: "Notifications" },
    { icon: <FaChartBar />, label: "Analytics" },
    { icon: <FaUser />, label: "Profile" },
  ];

  return (
    <div className="
      w-72
      min-h-screen
      bg-slate-800
      p-6
      flex
      flex-col
      shrink-0
    ">

      <div className="mb-12">
        <h1 className="text-3xl font-bold">
          CampusFlow
        </h1>

        <p className="text-slate-400 text-sm mt-1">
          SRM University
        </p>
      </div>

      <div className="space-y-3">
        {menuItems.map((item) => (
          <button
            key={item.label}
            className="
              w-full
              flex
              items-center
              gap-4
              p-4
              rounded-2xl
              hover:bg-slate-700
              transition
            "
          >
            <span className="text-xl">
              {item.icon}
            </span>

            <span>{item.label}</span>
          </button>
        ))}
      </div>
    </div>
  );
}

export default Sidebar;