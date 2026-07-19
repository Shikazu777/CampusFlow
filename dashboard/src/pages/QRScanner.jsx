import { useState } from "react";

import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";

import api from "../services/api";

function QRScanner() {

  const [qrCode, setQrCode] =
    useState("");

  async function scanQR() {

    try {

      const response =
        await api.post(
          "/orders/scan",
          {
            qr_code: qrCode
          }
        );

      alert(
        `Order ${response.data.order_id} collected`
      );

      setQrCode("");

    } catch (error) {



      alert("Invalid QR");
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
            QR Scanner
          </h1>

          <input
            type="text"
            placeholder="Paste QR code"
            value={qrCode}
            onChange={(e) =>
              setQrCode(
                e.target.value
              )
            }
            className="
              bg-slate-800
              p-4
              rounded-2xl
              w-[400px]
              mb-6
            "
          />

          <button
            onClick={scanQR}
            className="
              bg-blue-600
              px-8
              py-4
              rounded-2xl
            "
          >
            Scan QR
          </button>

        </div>

      </div>

    </div>
  );
}

export default QRScanner;