import api from "./api";

export async function addToCart(
  menuItemId
) {
  const userId =
    localStorage.getItem("user_id");

  const response = await api.post(
    "/cart/add-item",
    {
      user_id: Number(userId),
      menu_item_id: menuItemId,
      quantity: 1
    }
  );

  return response.data;
}