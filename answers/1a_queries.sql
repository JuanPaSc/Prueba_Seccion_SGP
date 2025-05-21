# ACTIVIDAD 1.a
# Cuáles son las ventas de cada uno de los productos vendidos por categoría y por cada uno de los vendedores, 
# indique aquí los nombres de estado civil sexo y tipo de identificación de cada vendedor en la consulta.
SELECT
    v.Identificacion AS ID_Vendedor,
    v.TipoIdentificacion,
    v.Nombre1,
    v.Nombre2,
    v.Apellido1,
    v.Apellido2,
    v.EstadoCivil,
    v.Sexo,
    c.Descripcion AS Categoria,
    p.Nombre AS Producto,
    SUM(dv.Cantidad) AS Total_Cantidad_Vendida,
    SUM(dv.Total) AS Total_Ventas
FROM
    TblDetalleVenta dv
    INNER JOIN TblVenta tv ON dv.IdFactura = tv.IdFactura
    INNER JOIN TblVendedor v ON tv.Vendedor = v.Identificacion
    INNER JOIN TblProducto p ON dv.IdProducto = p.IdProducto
    INNER JOIN TblCategoria c ON p.IdCategoria = c.IdCategoria
GROUP BY
    v.Identificacion,
    v.TipoIdentificacion,
    v.Nombre1,
    v.Nombre2,
    v.Apellido1,
    v.Apellido2,
    v.EstadoCivil,
    v.Sexo,
    c.Descripcion,
    p.Nombre
ORDER BY
    v.Identificacion,
    c.Descripcion,
    p.Nombre;