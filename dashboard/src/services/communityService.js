import api from "./api";

export async function getPosts() {
  const response = await api.get("/posts/");
  return response.data;
}

export async function createPost(postData) {
  const response = await api.post("/posts/", postData);
  return response.data;
}