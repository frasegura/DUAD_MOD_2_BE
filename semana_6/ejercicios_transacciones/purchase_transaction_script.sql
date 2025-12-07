
DO $$

BEGIN TRANSACTION
--a)User validation

	IF NOT EXISTS(SELECT from  transactions_ex.users WHERE user_id=1 ) THEN RAISE EXCEPTION 'The user does not exists';
	ELSE RAISE NOTICE 'The user exists';
	END IF;

--b)Product stock validation

	IF NOT EXISTS(SELECT FROM transactions_ex.products WHERE product_id=1 AND stock>0) THEN RAISE EXCEPTION 'Product not available';
	ELSE RAISE NOTICE 'Product available';
	END IF;

--c)Create Invoice for the related user
	INSERT INTO transactions_ex.invoice (invoice_date,user_id,status)
	VALUES('2025-11-19', 1, 'ACTIVA');
	
--c.1)Add invoice detail
	INSERT INTO transactions_ex.invoice_detail (amount,unit_price,total,invoice_id,product_id) VALUES (2,500,2*500,1,1);

--d)Reduce the stock
	UPDATE transactions_ex.products SET stock= stock-2 WHERE product_id = 1;
	
	SAVEPOINT invoice_created;
	
COMMIT;

END $$ LANGUAGE plpgsql;