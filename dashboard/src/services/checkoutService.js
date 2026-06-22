import api from "./api";

export async function checkoutCart(
  cartId
) {
  const response = await api.post(
    `/cart/checkout/${cartId}`,
    {
      coins_to_use: 0
    }
  );

  return response.data;
}