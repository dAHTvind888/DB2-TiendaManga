--Para que se pueda hacer un UPDATE, VendedorLogin necesita de poder hacer SELECT
--en la tabla Manga
GRANT SELECT ON dbo.Manga TO Vendedor;
--Para que se pueda hacer un UPDATE, VendedorLogin necesita de poder hacer SELECT
--en la tabla Volume
GRANT SELECT ON dbo.Volume TO Vendedor;
--Para que pueda realizar ventas
GRANT EXECUTE ON dbo.InsertarSales TO Vendedor;

GRANT EXECUTE ON dbo.InsertarDetails TO Vendedor;

