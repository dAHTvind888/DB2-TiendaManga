--View de Reporte para Mangas mas su total de ventas y total ganado
CREATE VIEW TopMangasVendidos AS
SELECT
    M.Manga_name, 
    SUM(S.Quantity) AS Total_Vendido,
    SUM(S.Quantity * V.Price) AS Total_Ganado
FROM manga AS M
INNER JOIN volume AS V ON V.Id_Manga = M.Id_Manga
INNER JOIN sales AS S ON S.Id_Volume = V.Id_Volume
GROUP BY M.Manga_name;

