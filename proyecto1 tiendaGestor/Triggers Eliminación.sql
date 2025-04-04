--Eliminar Customer
CREATE TRIGGER Eliminar_Customer
ON customer
INSTEAD OF DELETE
AS
BEGIN 
	SET NOCOUNT ON;
	DECLARE @IDCUSTOMER INT;
	SET @IDCUSTOMER = (SELECT Id_Customer FROM deleted);
	IF @IDCUSTOMER IN (SELECT Id_Customer FROM customer) AND @IDCUSTOMER  != 1
		BEGIN
		UPDATE SALES_DETAILS
		SET Id_Customer = 1
		WHERE Id_Customer = @IDCUSTOMER;

		DELETE FROM customer WHERE Id_Customer IN (SELECT Id_Customer FROM deleted);
		END
	ELSE
		PRINT('No existe Cliente')
		ROLLBACK;
END;

ALTER TRIGGER Eliminar_Customer
ON customer
INSTEAD OF DELETE
AS
BEGIN 
	SET NOCOUNT ON;
	DECLARE @IDCUSTOMER INT;
	SET @IDCUSTOMER = (SELECT Id_Customer FROM deleted);
	IF @IDCUSTOMER IN (SELECT Id_Customer FROM customer) AND @IDCUSTOMER  != 1
		BEGIN
		UPDATE sales_details
		SET Id_Customer = 1
		WHERE Id_Customer = @IDCUSTOMER;

		DELETE FROM customer WHERE Id_Customer IN (SELECT Id_Customer FROM deleted);
		END
	ELSE
		PRINT('No existe Cliente')
END;

--Eliminar Empleado
CREATE TRIGGER Eliminar_Employee
ON EMPLOYEE
INSTEAD OF DELETE
AS
BEGIN 
	SET NOCOUNT ON;
	DECLARE @IDEMPLOYEE INT;
	SET @IDEMPLOYEE = (SELECT Id_Employee FROM deleted);
	IF @IDEMPLOYEE IN (SELECT Id_Employee FROM EMPLOYEE) AND @IDEMPLOYEE  != 1
		BEGIN
		UPDATE SALES_DETAILS
		SET Id_Employee = 1
		WHERE Id_Employee = @IDEMPLOYEE;

		DELETE FROM EMPLOYEE WHERE Id_Employee IN (SELECT Id_Employee FROM deleted) AND Id_Employee != 1;
		END
	ELSE
		PRINT('No existe Empleado')
		ROLLBACK;
END;

--Eliminar Detalles
CREATE TRIGGER Eliminar_Details
ON SALES_DETAILS
INSTEAD OF DELETE
AS
BEGIN 
	SET NOCOUNT ON;
	DECLARE @SALES INT;
	SET @SALES = (SELECT Id_Sales FROM deleted);
	IF @SALES IN (SELECT Id_Sales FROM SALES_DETAILS)
		BEGIN
		
		SELECT Id_Volume, Quantity
		INTO #TEMP
		FROM SALES
		WHERE Id_Sales = @SALES;

		UPDATE V
		SET Stock = Stock + T.Quantity
		FROM VOLUME AS V
		INNER JOIN #TEMP AS T ON T.Id_Volume = V.Id_Volume;

		DELETE FROM SALES WHERE Id_Sales = @SALES;

		DELETE FROM SALES_DETAILS WHERE Id_Sales = @SALES;
		
		END
	ELSE
		PRINT('No existe Detalle de Venta')
		ROLLBACK;
END;

--Eliminar Ventas
CREATE TRIGGER Eliminar_Ventas
ON SALES
INSTEAD OF DELETE
AS
BEGIN 
	SET NOCOUNT ON;
	DECLARE @SALES INT;
	SET @SALES = (SELECT TOP 1 Id_Sales FROM deleted);
	IF @SALES IN (SELECT DISTINCT Id_Sales FROM SALES)
		BEGIN
		
		SELECT Id_Volume, Quantity
		INTO #TEMP
		FROM SALES
		WHERE Id_Sales = @SALES;

		UPDATE V
		SET Stock = Stock + T.Quantity
		FROM VOLUME AS V
		INNER JOIN #TEMP AS T ON T.Id_Volume = V.Id_Volume;

		DELETE FROM SALES WHERE Id_Sales = @SALES;

		DELETE FROM SALES_DETAILS WHERE Id_Sales = @SALES;
		
		END
	ELSE
		PRINT('No existe Venta')
		ROLLBACK;
END;

--Eliminar Volumen
CREATE TRIGGER Eliminar_Volumen
ON VOLUME
INSTEAD OF DELETE
AS
BEGIN 
	SET NOCOUNT ON;
	DECLARE @VOLUME INT;
	SET @VOLUME = (SELECT Id_Volume FROM deleted);
	IF @VOLUME IN (SELECT DISTINCT Id_Volume FROM VOLUME) AND @VOLUME != 1
		BEGIN
		
		UPDATE SALES
		SET Id_Volume = 1
		WHERE Id_Volume = @VOLUME;
		
		DELETE FROM VOLUME WHERE Id_Volume = @VOLUME;
		END
	ELSE
		PRINT('No existe Volumen')
		ROLLBACK;
END;

--Eliminar Manga
CREATE TRIGGER Eliminar_Manga
ON MANGA
INSTEAD OF DELETE
AS
BEGIN 
	SET NOCOUNT ON;
	DECLARE @MANGA INT;
	SET @MANGA = (SELECT Id_Manga FROM deleted);
	IF @MANGA IN (SELECT DISTINCT Id_Volume FROM VOLUME) AND @MANGA != 1
		BEGIN
		
		UPDATE VOLUME
		SET Id_Manga = 1
		WHERE Id_Manga = @MANGA;
		
		DELETE FROM MANGA WHERE Id_Manga = @MANGA;
		END
	ELSE
		PRINT('No existe Manga')
		ROLLBACK;
END;