function FoodCard({
  id,
  name,
  price,
  stall,
  onAdd
}){
  return (
    <div className="
      bg-slate-800
      rounded-3xl
      overflow-hidden
      shadow-lg
    ">

      <div className="
        h-48
        bg-slate-700
      " />

      <div className="p-5">

        <h2 className="text-xl font-bold">
          {name}
        </h2>

        <p className="text-slate-400 mt-2">
          {stall}
        </p>

        <div className="
          flex
          justify-between
          items-center
          mt-5
        ">

          <span className="text-2xl font-bold">
            ₹{price}
          </span>

          <button
            onClick={() => onAdd(id)}
            className="
            bg-blue-600
            px-5
            py-2
            rounded-xl
            hover:bg-blue-500
          ">
            Add
          </button>

        </div>

      </div>

    </div>
  );
}

export default FoodCard;