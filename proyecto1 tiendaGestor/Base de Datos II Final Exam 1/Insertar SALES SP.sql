ALTER PROCEDURE InsertarSales
	@Manga Varchar(100),
	@Volumen INT,
	@Cantidad INT
AS
BEGIN
	IF @Manga IN (SELECT Manga_name FROM MANGA) AND @Volumen IN (SELECT V.Volume_nro FROM VOLUME AS V INNER JOIN MANGA
	AS M ON V.Id_Manga = M.Id_Manga WHERE M.Manga_name = @Manga) AND (SELECT V.Estado FROM VOLUME AS V INNER JOIN MANGA
	AS M ON V.Id_Manga = M.Id_Manga WHERE M.Manga_name = @Manga AND V.Volume_nro = @Volumen) = 1
		BEGIN
		DECLARE @VOLUMEID INT = (SELECT V.Id_Volume FROM VOLUME AS V INNER JOIN MANGA AS M ON V.Id_Manga = M.Id_Manga WHERE M.Manga_name = @Manga AND V.Volume_nro = @Volumen)
		DECLARE @IDSALES INT;
		EXEC @IDSALES = DevolverIDMasReciente;
		INSERT INTO SALES(Id_Sales,Id_Volume,Quantity,Modified_date)
		VALUES(@IDSALES,@VOLUMEID,@Cantidad,GETDATE())
		END
	ELSE
		PRINT('Datos Erroneos')
END;