import { useEffect, useState } from "react";

import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";

import { useParams } from "react-router-dom";

import QRCode from "react-qr-code";

import { getOrder }
from "../services/orderService";

function QRPage() {

  const { orderId } =
    useParams();

  const [order, setOrder] =
    useState(null);

  useEffect(() => {
    loadOrder();
  }, []);

  async function loadOrder() {

    try {

      const data =
        await getOrder(orderId);

      setOrder(data);

    } catch (error) {

    }
  }

  if (!order) {
    return (
      <div className="
        min-h-screen
        bg-slate-900
        text-white
        flex
        items-center
        justify-center
      ">
        Loading QR...
      </div>
    );
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
          h-[80vh]
          flex
          flex-col
          justify-center
          items-center
        ">

          <h1 className="
            text-5xl
            font-bold
            mb-10
          ">
            Order QR
          </h1>

          <div className="
            bg-white
            p-8
            rounded-3xl
          ">

            <QRCode
              value={order.qr_code}
              size={300}
            />

          </div>

          <p className="
            mt-8
            text-slate-400
          ">
            Show this QR to the stall manager
          </p>

          <p className="
            mt-4
            text-xl
          ">
            QR:
          </p>

          <p className="
            text-sm
            text-slate-400
            mt-2
          ">
            {order.qr_code}
          </p>

        </div>

      </div>

    </div>
  );
}

export default QRPage;