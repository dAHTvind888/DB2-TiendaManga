CREATE TRIGGER Insertar_Sales
ON SALES
INSTEAD OF INSERT
AS
BEGIN
	SET NOCOUNT ON;
	DECLARE @Cant_Prod INT;
	DECLARE @Id_Vol INT;
	DECLARE @Id_Sale INT;
	SET @Cant_Prod = (SELECT Quantity FROM inserted);
	SET @Id_Vol = (SELECT Id_Volume FROM inserted);
	SET @Id_Sale = (SELECT Id_Sales FROM inserted);
	IF @Cant_Prod <= 0
		BEGIN
		PRINT('Cantidad Invalida')
		END
	ELSE IF @Id_Sale IN (SELECT Id_Sales FROM SALES_DETAILS)
		BEGIN
		IF @Cant_Prod <= (SELECT Stock FROM VOLUME WHERE Id_Volume = @Id_Vol)
			BEGIN
			UPDATE VOLUME
			SET Stock = Stock - @Cant_Prod
			WHERE Id_Volume = @Id_Vol
			

			INSERT INTO SALES (Id_Sales, Id_Volume, Quantity)
			SELECT Id_Sales, Id_Volume, Quantity
			FROM inserted

			UPDATE SALES
			SET Modified_date = GETDATE()
			WHERE Id_Sales = (SELECT Id_Sales FROM inserted) AND Id_Volume = (SELECT Id_Volume FROM inserted)

			DECLARE @PRECIO INT = (SELECT Price FROM VOLUME WHERE Id_Volume = @Id_Vol)

			UPDATE SALES_DETAILS
			SET Total_price = Total_price + (@Cant_Prod * @PRECIO)
			WHERE Id_Sales = @Id_Sale;

			END
		ELSE
			BEGIN
			PRINT('Supera al Stock')
			END
		END
	ELSE
		BEGIN
		PRINT('No existe Id_Sales')
		DECLARE @LAST INT = (SELECT TOP 1 Id_Sales FROM SALES_DETAILS ORDER BY 1 DESC)
		PRINT('ÚLTIMO ID_SALES_DETAILS: ')
		PRINT(@LAST)
		END
END;

CREATE TRIGGER Insertar_Sales_Details
ON SALES_DETAILS
INSTEAD OF INSERT
AS
BEGIN
	IF (SELECT Id_Customer FROM inserted) IS NULL AND (SELECT Id_Employee FROM inserted) IN (SELECT Id_Employee FROM EMPLOYEE)
	AND (SELECT Estado FROM EMPLOYEE where Id_Employee = (SELECT Id_Employee FROM inserted)) = 1
		INSERT INTO SALES_DETAILS(Id_Employee,Sales_date,Total_price, Modified_date)
		VALUES((SELECT Id_Employee FROM inserted), (SELECT Sales_date FROM inserted), 0, GETDATE());
	ELSE IF (SELECT Id_Customer FROM inserted) IN (SELECT Id_Customer FROM CUSTOMER) AND (SELECT Id_Employee FROM inserted) IN (SELECT Id_Employee FROM EMPLOYEE)
	AND (SELECT Estado FROM EMPLOYEE where Id_Employee = (SELECT Id_Employee FROM inserted)) = 1
		INSERT INTO SALES_DETAILS(Id_Customer,Id_Employee,Sales_date,Total_price, Modified_date)
		VALUES((SELECT Id_Customer FROM inserted),(SELECT Id_Employee FROM inserted), (SELECT Sales_date FROM inserted), 0, GETDATE());
	ELSE
		PRINT('NO EXISTE CLIENTE O EMPLEADO')
END;