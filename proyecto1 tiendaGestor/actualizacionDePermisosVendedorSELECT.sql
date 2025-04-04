--Para que se pueda hacer un UPDATE, VendedorLogin necesita de poder hacer SELECT
--en la tabla Manga
GRANT SELECT ON dbo.Manga TO Vendedor;
--Para que se pueda hacer un UPDATE, VendedorLogin necesita de poder hacer SELECT
--en la tabla Volume
GRANT SELECT ON dbo.Volume TO Vendedor;

