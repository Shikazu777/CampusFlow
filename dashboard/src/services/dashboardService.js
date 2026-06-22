import api from "./api";

export async function getDashboardData() {
  const userId =
    localStorage.getItem("user_id");

  const response = await api.get(
    `/users/${userId}/dashboard`
  );

  return response.data;
}