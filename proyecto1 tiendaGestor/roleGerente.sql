--Crear usuario Gerente
CREATE LOGIN GerenteLogin WITH PASSWORD = '1234';
CREATE USER Gerente FOR LOGIN GerenteLogin;

GRANT SELECT ON dbo.TopMangasVendidos TO Gerente;
GRANT SELECT ON dbo.VentasPorManga TO Gerente;

