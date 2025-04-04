--Crear usuario DBA que tiene acceso completo a la base de datos
CREATE LOGIN DBALogin WITH PASSWORD = '12345';
CREATE USER DBA FOR LOGIN DBALogin;
ALTER ROLE db_owner ADD MEMBER DBA;
