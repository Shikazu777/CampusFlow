import api from "./api";

export async function getFoods() {
  const response = await api.get(
    "/menu-items/"
  );

  return response.data;
}