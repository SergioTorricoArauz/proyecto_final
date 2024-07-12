import React, { useEffect, useState } from "react";
import { getResumenVentaV, anularVenta } from "../../service/surtidorService";
import { Venta } from "../../models/venta";

const ResumenVentaV: React.FC = () => {
  const [resumenventas, setResumenventas] = useState<Venta[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    getResumenVentaV()
      .then((data) => {
        setResumenventas(data);
        setError(null);
      })
      .catch((error) => {
        setError(error.message);
      });
  }, []);

  const handleAnular = (ventaId: number) => {
    const confirmAnular = window.confirm(
      "¿Está seguro de que desea anular esta venta?"
    );
    if (confirmAnular) {
      anularVenta(ventaId)
        .then(() => {
          setResumenventas(
            resumenventas.map((venta) =>
              venta.id === ventaId
                ? { ...venta, estado_display: "Anulado" }
                : venta
            )
          );
        })
        .catch((error) => {
          setError(error.message);
        });
    }
  };

  return (
    <div className="container mt-5">
      <h2>Resumen de Ventas</h2>
      {error && <div className="alert alert-danger">{error}</div>}
      <table className="table table-striped mt-3">
        <thead>
          <tr>
            <th>ID</th>
            <th>Factura</th>
            <th>Cliente</th>
            <th>Correo</th>
            <th>Precio</th>
            <th>Precio U/L</th>
            <th>Litros</th>
            <th>Producto</th>
            <th>Bomba</th>
            <th>Estado</th>
            <th>Total</th>
            <th>Fecha de venta</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {resumenventas.map((venta) => (
            <tr key={venta.id}>
              <td>{venta.id}</td>
              <td>{venta.nombre_factura}</td>
              <td>{venta.cliente}</td>
              <td>{venta.correo}</td>
              <td className="text-nowrap">{venta.precio_actual_producto}</td>
              <td className="text-nowrap">{venta.cantidad_producto_litros}</td>
              <td className="text-nowrap">{venta.tipo_producto.nombre}</td>
              <td className="text-nowrap">{venta.bomba.codigo}</td>
              <td className="text-nowrap">{venta.estado_display}</td>
              <td className="text-nowrap">{venta.monto}</td>
              <td className="text-nowrap">
                {new Date(venta.fecha_hora).toLocaleDateString()}
              </td>
              <td className="text-nowrap">
                <button
                  className={`btn ${
                    venta.estado_display === "Anulado"
                      ? "btn-secondary"
                      : "btn-danger"
                  }`}
                  onClick={() => handleAnular(venta.id)}
                  disabled={venta.estado_display === "Anulado"}
                >
                  {venta.estado_display === "Anulado" ? "Anulada" : "Anular"}
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ResumenVentaV;
