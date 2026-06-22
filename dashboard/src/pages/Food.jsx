import { useEffect, useState } from "react";

import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";
import FoodCard from "../components/FoodCard";

import { getFoods }
from "../services/foodService";
import { addToCart }
from "../services/cartService";

function Food() {

  const [foods, setFoods] =
    useState([]);

  useEffect(() => {
    loadFoods();
  }, []);

  async function loadFoods() {
    try {

      const data =
        await getFoods();

      setFoods(data);

    } catch (error) {
      console.log(error);
    }
  }
  async function handleAddToCart(
  menuItemId
) {
  try {

    await addToCart(menuItemId);

    alert("Added to cart");

  } catch (error) {

    console.log(error);

    alert("Failed");

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
          Campus Food
        </h1>

        <div className="
          grid
          grid-cols-1
          md:grid-cols-2
          xl:grid-cols-3
          gap-6
        ">

          {foods.map((food) => (
            <FoodCard
  key={food.id}
  id={food.id}
  name={food.name}
  price={food.price}
  stall="Campus Stall"
  onAdd={handleAddToCart}
/>
          ))}

        </div>

      </div>

    </div>
  );
}

export default Food;