import { useEffect, useState } from "react";

import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";

import api from "../services/api";

function MyOrders() {

  const [orders, setOrders] =
    useState([]);

  useEffect(() => {
    loadOrders();
  }, []);

  async function loadOrders() {

    try {

      const userId =
        localStorage.getItem(
          "user_id"
        );

      const response =
        await api.get(
          `/orders/my-orders/${userId}`
        );

      setOrders(
        response.data
      );

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

        <h1 className="
          text-4xl
          font-bold
          mb-8
        ">
          My Orders
        </h1>

        <div className="space-y-5">

          {orders.map((order) => (

            <div
              key={order.id}
              className="
                bg-slate-800
                p-6
                rounded-3xl
                flex
                justify-between
                items-center
              "
            >

              <div>

                <h2 className="
                  text-2xl
                  font-semibold
                ">
                  Order #{order.id}
                </h2>

                <p className="text-slate-400">
                  ₹{order.total_amount}
                </p>

                <p className="text-slate-400">
                  Status:
                  {" "}
                  {order.status}
                </p>

                <p className="text-slate-400">
                  Pickup:
                  {" "}
                  {order.pickup_status}
                </p>

              </div>

            </div>

          ))}

        </div>

      </div>

    </div>
  );
}

export default MyOrders;