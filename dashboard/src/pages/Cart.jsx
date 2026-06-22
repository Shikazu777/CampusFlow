import { useEffect, useState } from "react";

import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";

import { getMyCarts }
from "../services/myCartService";

import { getCartDetails }
from "../services/cartDetailsService";

import { checkoutCart }
from "../services/checkoutService";

import { useNavigate }
from "react-router-dom";

function Cart() {

  const [cart, setCart] =
    useState(null);

  useEffect(() => {
    loadCart();
  }, []);

  async function loadCart() {

    try {

      const carts =
        await getMyCarts();

      if (carts.length === 0) {
        return;
      }

      const details =
        await getCartDetails(
          carts[0].id
        );

      setCart(details);

    } catch (error) {
      console.log(error);
    }
  }

  const navigate = useNavigate();

  async function handleCheckout() {

  try {

    const response =
      await checkoutCart(
        cart.cart_id
      );

    navigate(
      `/payment/${response.order_id}`
    );

  } catch (error) {

    console.log(error);

    alert(
      "Checkout failed"
    );
  }
}

  if (!cart) {
    return (
      <div className="
        min-h-screen
        bg-slate-900
        text-white
        flex
        items-center
        justify-center
      ">
        Cart Empty
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

        <h1 className="
          text-4xl
          font-bold
          mb-8
        ">
          My Cart
        </h1>

        <div className="space-y-5">

          {cart.items.map((item) => (

            <div
              key={item.menu_item_id}
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
                  {item.name}
                </h2>

                <p className="text-slate-400">
                  Quantity: {item.quantity}
                </p>

                <p className="text-slate-400">
                  ₹{item.price} each
                </p>

              </div>

              <div className="
                text-2xl
                font-bold
              ">
                ₹{item.subtotal}
              </div>

            </div>

          ))}

        </div>

        <div className="
          mt-8
          bg-slate-800
          p-6
          rounded-3xl
          flex
          justify-between
          items-center
        ">

          <h2 className="
            text-3xl
            font-bold
          ">
            Total:
            ₹{cart.total}
          </h2>

          <button
  onClick={handleCheckout}
  className="
    bg-blue-600
    px-8
    py-4
    rounded-2xl
    hover:bg-blue-500
  "
>
  Checkout
</button>

        </div>

      </div>

    </div>
  );
}

export default Cart;