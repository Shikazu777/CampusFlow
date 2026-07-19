import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
  timeout: 30000 // 30 second timeout for all requests
});

api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("token");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor for error handling
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.code === 'ECONNABORTED') {
      error.message = 'Request timeout - server not responding';
    } else if (error.response?.status === 401) {
      localStorage.removeItem("token");
      window.location.href = "/";
    } else if (error.response?.status === 403) {
      error.message = 'Access denied - insufficient permissions';
    }
    return Promise.reject(error);
  }
);

export default api;
