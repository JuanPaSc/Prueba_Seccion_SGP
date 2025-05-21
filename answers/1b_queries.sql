# ACTIVIDAD 1.b
# Cuáles son los productos que han tenido mayor venta y a qué vendedor pertenece?
SELECT
    p.Nombre AS Producto,
    v.Identificacion AS ID_Vendedor,
    v.Nombre1,
    v.Nombre2,
    v.Apellido1,
    v.Apellido2,
    SUM(dv.Total) AS Total_Ventas
FROM
    TblDetalleVenta dv
    INNER JOIN TblVenta tv ON dv.IdFactura = tv.IdFactura
    INNER JOIN TblVendedor v ON tv.Vendedor = v.Identificacion
    INNER JOIN TblProducto p ON dv.IdProducto = p.IdProducto
GROUP BY
    p.Nombre,
    v.Identificacion,
    v.Nombre1,
    v.Nombre2,
    v.Apellido1,
    v.Apellido2
ORDER BY
    Total_Ventas DESC;