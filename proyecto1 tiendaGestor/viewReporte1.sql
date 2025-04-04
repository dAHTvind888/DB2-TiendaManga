--Reporte: total vendido por manga y volumen en un dia en especifico
CREATE VIEW VentasPorManga AS
SELECT 
    M.Manga_name, 
    V.Volume_nro, 
    SD.Sales_date,
    SUM(V.Price * S.Quantity) AS 'Precio total ganado'
FROM manga AS M
INNER JOIN volume AS V ON V.Id_Manga = M.Id_Manga
INNER JOIN sales AS S ON S.Id_Volume = V.Id_Volume
INNER JOIN sales_details AS SD ON SD.Id_Sales = S.Id_Sales
GROUP BY M.Manga_name, V.Volume_nro, SD.Sales_date;


--select * from VentasPorManga
--WHERE Sales_date = '2024-12-06'