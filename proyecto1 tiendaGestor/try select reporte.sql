--Reporte: total vendido por manga y volumen en un dia en especifico
SELECT M.Manga_name, V.Volume_nro, SUM(V.Price * S.Quantity) AS 'Precio total ganado'
FROM manga AS M
INNER JOIN volume AS V ON V.Id_Manga = M.Id_Manga
INNER JOIN sales AS S ON S.Id_Volume = V.Id_Volume
INNER JOIN sales_details AS SD ON SD.Id_Sales = S.Id_Sales
--WHERE SD.Sales_date = '2024-12-06'
GROUP BY M.Manga_name, V.Volume_nro;

DECLARE @date
WHERE SD.Sales_date = @date