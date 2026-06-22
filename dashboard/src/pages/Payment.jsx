import { useEffect } from "react";

import {
  useNavigate,
  useParams
} from "react-router-dom";

import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";

import { paymentSuccess }
from "../services/paymentService";

function Payment() {

  const navigate = useNavigate();

  const { orderId } =
    useParams();

  useEffect(() => {

    async function processPayment() {

      try {

        await paymentSuccess(
          orderId
        );

        setTimeout(() => {

          navigate(
            `/qr/${orderId}`
          );

        }, 7000);

      } catch (error) {

        console.log(error);

        alert(
          "Payment failed"
        );
      }
    }

    processPayment();

  }, []);

  return (
    <div className="
      flex
      bg-slate-900
      min-h-screen
      text-white
    ">

      <Sidebar />

      <div className="
        flex-1
        p-8
      ">

        <Navbar />

        <div className="
          h-[70vh]
          flex
          flex-col
          justify-center
          items-center
        ">

          <div className="
            h-32
            w-32
            rounded-full
            border-8
            border-blue-500
            animate-pulse
          " />

          <h1 className="
            text-5xl
            font-bold
            mt-10
          ">
            Processing Payment...
          </h1>

          <p className="
            text-slate-400
            mt-4
          ">
            Redirecting shortly
          </p>

        </div>

      </div>

    </div>
  );
}

export default Payment;