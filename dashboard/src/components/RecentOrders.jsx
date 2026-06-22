function RecentOrders() {
  const orders = [
    {
      id: 1,
      item: "Chicken Biryani",
      amount: "₹120",
      status: "Delivered"
    },
    {
      id: 2,
      item: "Cold Coffee",
      amount: "₹60",
      status: "Preparing"
    },
    {
      id: 3,
      item: "Masala Dosa",
      amount: "₹80",
      status: "Delivered"
    }
  ];

  return (
    <div className="bg-slate-800 rounded-3xl p-6">

      <h2 className="text-2xl font-bold mb-6">
        Recent Orders
      </h2>

      <div className="space-y-4">

        {orders.map((order) => (
          <div
            key={order.id}
            className="
              flex
              justify-between
              items-center
              bg-slate-700
              p-4
              rounded-2xl
            "
          >
            <div>
              <h3 className="font-semibold">
                {order.item}
              </h3>

              <p className="text-slate-400">
                {order.amount}
              </p>
            </div>

            <span
              className="
                bg-green-600
                px-3
                py-1
                rounded-full
                text-sm
              "
            >
              {order.status}
            </span>

          </div>
        ))}

      </div>
    </div>
  );
}

export default RecentOrders;