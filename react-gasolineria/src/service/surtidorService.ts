import { Venta } from "../models/venta";

const API_URL = "http://127.0.0.1:8001/api";

export const getResumenVentaV = (): Promise<Venta[]> => {
  const token = localStorage.getItem("token");

  return fetch(`${API_URL}/venta`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
  }).then((response) => {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.json();
  });
};

export const anularVenta = (ventaId: number): Promise<void> => {
  const token = localStorage.getItem("token");

  return fetch(`${API_URL}/anular_venta/${ventaId}/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
  }).then((response) => {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
  });
};
