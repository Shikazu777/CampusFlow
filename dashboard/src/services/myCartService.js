import api from "./api";

export async function getMyCarts() {
  const userId =
    localStorage.getItem("user_id");

  const response = await api.get(
    `/cart/my-carts/${userId}`
  );

  return response.data;
}