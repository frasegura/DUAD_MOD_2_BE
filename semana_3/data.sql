-- SQLite

INSERT INTO products (code,name,price,admission_date,brand)
    VALUES (001,'Computer',700,'2025-09-13','HP')

INSERT INTO products (code,name,price,admission_date,brand)
    VALUES (002,'Mouse',20,'2025-08-13','HP')

INSERT INTO products (code,name,price,admission_date,brand)
    VALUES (003,'keyboard',20,'2025-10-13','DELL')

INSERT INTO products (code,name,price,admission_date,brand)
    VALUES (004,'Monitor',1000,'2025-01-13','Apple')


-- Pmnt methods linked with each user

INSERT INTO payment_method(method_type,bank_name,user_id)
	values('Credit Card','BAC',1);


INSERT INTO payment_method(method_type,bank_name,user_id)
	values('Credit Card','Banco Popular',2);


INSERT INTO payment_method(method_type,bank_name,user_id)
	values('Credit Card','Lafise',1);


INSERT INTO payment_method(method_type,bank_name,user_id)
	values('Credit Card','Scotia Bank',3);

INSERT INTO payment_method(method_type,bank_name,user_id)
	values('Credit Card','Davivienda',4);

--

INSERT INTO invoice(invoice_number, purchase_date,total_amount,cx_phone_number,employee_code,user_id,pmnt_method_id)
	values(124,'2025-09-13',700, '89559579', '756C',1,1);

--

INSERT INTO invoice_detail(quantity,subtotal,invoice_id,product_id)
	values(1,70000,2,8);

INSERT INTO invoice_detail(quantity,subtotal,invoice_id,product_id)
	values(1,60000,3,9);