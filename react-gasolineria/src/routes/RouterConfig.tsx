import { createBrowserRouter } from "react-router-dom";
import LoginPage from "../pages/auth/LoginPage";
import ResumenVentaV from "../pages/surtidor/ResumenVentaV";

// Función de ejemplo que maneja el éxito del login
const handleLoginSuccess = () => {
  console.log("Login exitoso");
};

export const routerConfig = createBrowserRouter([
  {
    path: "/",
    element: <LoginPage onLoginSuccess={handleLoginSuccess} />,
  },
  {
    path: "/surtidor/venta/list",
    element: <ResumenVentaV />,
  },
]);
