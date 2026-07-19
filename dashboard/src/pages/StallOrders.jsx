import { useEffect, useState } from "react";

import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";

import api from "../services/api";

function StallOrders() {

  const [orders, setOrders] =
    useState([]);

  useEffect(() => {
    loadOrders();
  }, []);

  async function loadOrders() {

    try {

      // Temporary stall id = 1

      const response = await api.get(
        "/orders/stall/1"
      );

      setOrders(
        response.data
      );

    } catch (error) {

    }
  }

  async function markReady(
    orderId
  ) {

    try {

      await api.post(
        `/orders/${orderId}/ready`
      );

      loadOrders();

    } catch (error) {


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
          Stall Orders
        </h1>

        <div className="space-y-5">

          {orders.map((order) => (

            <div
              key={order.order_id}
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
                  Order #
                  {order.order_id}
                </h2>

                <p className="text-slate-400">
                  {order.student_name}
                </p>

                <p className="text-slate-400">
                  ₹{order.total_amount}
                </p>

              </div>

              <button
                onClick={() =>
                  markReady(
                    order.order_id
                  )
                }
                className="
                  bg-green-600
                  px-6
                  py-3
                  rounded-2xl
                "
              >
                Mark Ready
              </button>

            </div>

          ))}

        </div>

      </div>

    </div>
  );
}

export default StallOrders;