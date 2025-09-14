-- 1. Obtenga todos los productos almacenados

SELECT * FROM products

--2. Obtenga todos los productos que tengan un precio mayor a 50000

SELECT * 
	FROM products
	WHERE price > 50000

-- 3. Obtenga todas las compras de un mismo producto por id.

SELECT *
	FROM invoice_detail
	WHERE id = 2

SELECT *
	FROM invoice_detail
	WHERE id = 3


-- 4. Obtenga todas las compras agrupadas por producto, donde se muestre el total comprado entre todas las compras.

FALTA


-- 5. Obtenga todas las facturas realizadas por el mismo comprador

SELECT * FROM invoice WHERE user_id = 2


-- 6. Obtenga todas las facturas ordenadas por monto total de forma descendente

SELECT * 
	FROM invoice
	ORDER BY total_amount DESC


-- 7. Obtenga una sola factura por número de factura.

SELECT *
	FROM invoice
	WHERE invoice_number = 124