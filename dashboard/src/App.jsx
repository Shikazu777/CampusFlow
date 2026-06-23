import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import Food from "./pages/Food";
import ProtectedRoute from "./components/ProtectedRoute";
import Cart from "./pages/Cart";    
import QRPage from "./pages/QRPage";
import StallOrders
from "./pages/StallOrders";
import QRScanner
from "./pages/QRScanner";
import MyOrders
from "./pages/MyOrders";
import Community
from "./pages/Community";
import CreatePost
from "./pages/CreatePost";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/"
          element={<Login />}
        />

        <Route
          path="/register"
          element={<Register />}
        />

        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          }
        />

        <Route
  path="/cart"
  element={
    <ProtectedRoute>
      <Cart />
    </ProtectedRoute>
  }
/>

<Route
  path="/qr/:orderId"
  element={
    <ProtectedRoute>
      <QRPage />
    </ProtectedRoute>
  }
/>

        <Route
        
  path="/food"
  element={
    <ProtectedRoute>
      <Food />
    </ProtectedRoute>
  }
/>
<Route
  path="/stall-orders"
  element={
    <ProtectedRoute>
      <StallOrders />
    </ProtectedRoute>
  }
/>
<Route
  path="/scan"
  element={
    <ProtectedRoute>
      <QRScanner />
    </ProtectedRoute>
  }
/>
<Route
  path="/my-orders"
  element={
    <ProtectedRoute>
      <MyOrders />
    </ProtectedRoute>
  }
/>
<Route
  path="/community"
  element={
    <ProtectedRoute>
      <Community />
    </ProtectedRoute>
  }
/>
<Route
  path="/create-post"
  element={
    <ProtectedRoute>
      <CreatePost />
    </ProtectedRoute>
  }
/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;