import { useState } from "react";
import { useNavigate } from "react-router-dom";

import api from "../services/api";

function Login() {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  async function handleLogin(e) {
    e.preventDefault();
    setError("");

    try {
      const response = await api.post(
        "/auth/login",
        {
          email,
          password
        }
      );

      const token = response.data.access_token;
      localStorage.setItem("token", token);

      const payload = JSON.parse(
        atob(
          token.split(".")[1]
        )
      );

      localStorage.setItem(
        "user_id",
        payload.sub
      );

      navigate("/dashboard");

    } catch (error) {
      const errorMsg = error.response?.data?.detail || "Login failed. Please try again.";
      setError(errorMsg);
    }
  }

  return (
    <div>
      <h1>CampusFlow Login</h1>

      {error && <div style={{ color: "red", marginBottom: "10px" }}>{error}</div>}

      <form onSubmit={handleLogin}>
        <div>
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) =>
              setEmail(e.target.value)
            }
            required
          />
        </div>

        <br />

        <div>
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) =>
              setPassword(e.target.value)
            }
            required
          />
        </div>

        <br />

        <button type="submit">
          Login
        </button>
      </form>
    </div>
  );
}

export default Login;