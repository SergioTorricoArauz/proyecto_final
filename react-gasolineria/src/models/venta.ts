export interface Venta {
  id: number;
  nombre_factura: string;
  cliente: string;
  correo: string;
  monto: number;
  precio_actual_producto: number;
  cantidad_producto_litros: number;
  tipo_producto: TipoProducto;
  bomba: Bomba;
  fecha_hora: Date;
  estado_display: string;
}

export interface Bomba {
  codigo: string;
}

export interface TipoProducto {
  nombre: string;
}
