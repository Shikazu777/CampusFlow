import { useState } from "react";
import { useNavigate } from "react-router-dom";

import api from "../services/api";

function Login() {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  async function handleLogin(e) {
    e.preventDefault();

    try {
      const response = await api.post(
        "/auth/login",
        {
          email,
          password
        }
      );

      localStorage.setItem(
        "token",
        response.data.access_token
      );

      const payload = JSON.parse(
        atob(
          response.data.access_token.split(".")[1]
        )
      );

      console.log(payload);

      localStorage.setItem(
        "user_id",
        payload.sub
      );

      navigate("/dashboard");

    } catch (error) {
      console.log(error);

      alert(
        error.response?.data?.detail ||
        "Invalid credentials"
      );
    }
  }

  return (
    <div>
      <h1>CampusFlow Login</h1>

      <form onSubmit={handleLogin}>
        <div>
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) =>
              setEmail(e.target.value)
            }
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