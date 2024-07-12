import axios from "axios";

const API_URL = "http://127.0.0.1:8000/api/token/"; // Reemplaza con la URL de tu API

export const login = (username: string, password: string): Promise<string> => {
  return axios.post(API_URL, { username, password }).then((response) => {
    const token = response.data?.access;
    if (token) {
      localStorage.setItem("token", token); // Guarda el token en localStorage
      return token;
    }
    throw new Error("Invalid email or password");
  });
};
