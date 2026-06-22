import api from "./api";

export async function paymentSuccess(
  orderId
) {
  const response = await api.post(
    `/orders/${orderId}/payment-success`
  );

  return response.data;
}