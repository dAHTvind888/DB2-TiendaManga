CREATE PROCEDURE InsertarDetails
	@NIT INT,
	@EmpleadoID INT
AS
BEGIN
	IF @NIT IS NULL AND @EmpleadoID IN (SELECT Id_Employee FROM EMPLOYEE)
	AND (SELECT Estado FROM EMPLOYEE WHERE Id_Employee = @EmpleadoID) = 1
		BEGIN
		INSERT INTO SALES_DETAILS(Id_Employee,Sales_date, Total_price, Modified_date)
		VALUES(@EmpleadoID,GETDATE(),0,GETDATE())
		END
	ELSE IF @NIT IN (SELECT NIT FROM CUSTOMER) AND @EmpleadoID IN (SELECT Id_Employee FROM EMPLOYEE)
	AND (SELECT Estado FROM EMPLOYEE WHERE Id_Employee = @EmpleadoID) = 1
		BEGIN
		DECLARE @ID_CUS INT = (SELECT Id_Customer FROM CUSTOMER WHERE NIT = @NIT);
		INSERT INTO SALES_DETAILS(Id_Customer,Id_Employee,Sales_date, Total_price, Modified_date)
		VALUES(@ID_CUS, @EmpleadoID,GETDATE(),0,GETDATE())
		END
	ELSE
		PRINT('Datos Incorrectos')
END;