CREATE LOGIN VendedorLogin WITH PASSWORD = '123';
CREATE USER Vendedor FOR LOGIN VendedorLogin;

GRANT INSERT ON dbo.manga TO Vendedor;
GRANT INSERT ON dbo.volume TO Vendedor;
GRANT INSERT ON dbo.sales TO Vendedor;
GRANT INSERT ON dbo.sales_details TO Vendedor;
GRANT INSERT ON dbo.customer TO Vendedor;

GRANT UPDATE ON dbo.manga TO Vendedor;
GRANT UPDATE ON dbo.volume TO Vendedor;