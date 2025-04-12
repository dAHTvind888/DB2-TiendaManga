CREATE PROCEDURE DevolverPrecio
	@Manga Varchar(100),
	@Volume INT
AS
BEGIN
	DECLARE @PRECIO INT = (SELECT V.Price FROM VOLUME AS V INNER JOIN MANGA AS M ON V.Id_Manga = M.Id_Manga AND V.Volume_nro = @Volume AND M.Manga_name = @Manga);
	RETURN @PRECIO;
END

DECLARE @PRI INT;
EXEC @PRI = DevolverPrecio 'One Piece',2;
SELECT @PRI;