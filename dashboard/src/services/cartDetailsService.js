import api from "./api";

export async function getCartDetails(
  cartId
) {
  const response = await api.get(
    `/cart/${cartId}`
  );

  return response.data;
}