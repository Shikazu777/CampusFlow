import { useEffect, useState } from "react";

import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";
import StatCard from "../components/StatCard";
import RecentOrders from "../components/RecentOrders";
import UpcomingEvents from "../components/UpcomingEvents";
import CommunityPreview from "../components/CommunityPreview";

import { getDashboardData }
from "../services/dashboardService";

function Dashboard() {
  const [dashboard, setDashboard] =
  useState(null);

useEffect(() => {
  loadDashboard();
}, []);

async function loadDashboard() {
  try {
    const data =
      await getDashboardData();

    setDashboard(data);

  } catch (error) {

  }
}
if (!dashboard) {
  return (
    <div className="
      min-h-screen
      bg-slate-900
      text-white
      flex
      items-center
      justify-center
    ">
      Loading...
    </div>
  );
}
  return (
    <div className="flex bg-slate-900 min-h-screen text-white">

      <Sidebar />

      <div className="flex-1 p-8 overflow-y-auto">

        <Navbar />

        {/* Stats */}
        <div className="
          grid
          grid-cols-1
          md:grid-cols-2
          xl:grid-cols-4
          gap-6
        ">
          <StatCard
  title="Coins"
  value={dashboard.coins}
/>

<StatCard
  title="Trust Score"
  value={dashboard.trust_score}
/>

<StatCard
  title="Orders"
  value={dashboard.total_orders}
/>

<StatCard
  title="Events Attended"
  value={dashboard.events_attended}
/>
        </div>

        {/* Orders + Events */}
        <div className="
          grid
          grid-cols-1
          xl:grid-cols-2
          gap-6
          mt-8
        ">
          <RecentOrders />
          <UpcomingEvents />
        </div>

        {/* Community */}
        <div className="mt-8">
          <CommunityPreview />
        </div>

      </div>

    </div>
  );
}

export default Dashboard;