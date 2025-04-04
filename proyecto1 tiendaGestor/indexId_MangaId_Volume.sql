/*
Indices creados en Id_Manga y Id_Volume
para una ejecucion mas rapida de TopMangasVendidos
Razon del indice: ambas columnas se usan el los inner join
				  de TopMangasVendidos
*/
CREATE INDEX idx_sales_IdVolume ON sales(Id_Volume);
CREATE INDEX idx_volume_IdManga ON volume(Id_Manga);
