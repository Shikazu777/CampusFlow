import api from "./api";

export async function getOrder(
  orderId
) {
  const response = await api.get(
    `/orders/${orderId}`
  );

  return response.data;
}