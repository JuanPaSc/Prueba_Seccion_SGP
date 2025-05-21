# ACTIVIDAD 1.c
# Construya una consulta general que involucre todas las tablas del Modelo Relacional y permita visualizar totales en ella.
SELECT
    tv.IdFactura,
    tv.Fecha,
    tv.IVA,
    v.Identificacion AS ID_Vendedor,
    v.TipoIdentificacion,
    v.Nombre1,
    v.Nombre2,
    v.Apellido1,
    v.Apellido2,
    v.EstadoCivil,
    v.Sexo,
    p.IdProducto,
    p.Nombre AS Producto,
    p.Descripcion AS DescripcionProducto,
    c.Descripcion AS CategoriaProducto,
    dv.Cantidad,
    dv.Total AS TotalPorProducto,
    cd.NombreConcepto AS DetalleConcepto,
    co.NombreConcepto AS Concepto,
    (dv.Total + tv.IVA) AS TotalConIVA
FROM
    TblVenta tv
    INNER JOIN TblVendedor v ON tv.Vendedor = v.Identificacion
    INNER JOIN TblDetalleVenta dv ON tv.IdFactura = dv.IdFactura
    INNER JOIN TblProducto p ON dv.IdProducto = p.IdProducto
    INNER JOIN TblCategoria c ON p.IdCategoria = c.IdCategoria
    LEFT JOIN TblConceptoDetalle cd ON cd.IdDetalleConcepto = tv.IdTienda
    LEFT JOIN TblConcepto co ON co.IdConcepto = cd.IdConcepto
ORDER BY
    tv.IdFactura,
    p.Nombre;