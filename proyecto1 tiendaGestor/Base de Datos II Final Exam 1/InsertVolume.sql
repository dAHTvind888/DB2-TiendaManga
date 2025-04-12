CREATE TRIGGER InsertarVolume
ON VOLUME
AFTER INSERT
AS
BEGIN
	SET NOCOUNT ON
	IF((SELECT Estado FROM MANGA WHERE Id_Manga = (Select Id_Manga FROM inserted))) = 0
		BEGIN
		UPDATE VOLUME
		SET Estado = 0
		WHERE Id_Volume = (SELECT Id_Volume FROM inserted)
		END
	ELSE
		UPDATE VOLUME
		SET Estado = 1
		WHERE Id_Volume = (SELECT Id_Volume FROM inserted)
END