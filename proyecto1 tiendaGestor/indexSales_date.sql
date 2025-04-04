--Crear indice para una ejecucion mas rapida en el view VentasPorManga
--Crear el indice en Sales_date de la tabla sales_details
--ya que se hara un select a VentasPorManga en una fecha en especifico
CREATE INDEX idx_SalesDate ON sales_details(Sales_date);