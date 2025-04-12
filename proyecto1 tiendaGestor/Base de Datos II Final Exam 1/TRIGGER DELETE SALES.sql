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
END;