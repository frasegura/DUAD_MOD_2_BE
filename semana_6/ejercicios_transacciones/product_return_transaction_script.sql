DO $$
DECLARE 
    v_invoice_id INT := 1;
    v_product_id INT;
    v_amount INT;
	
BEGIN

--a. Invoice existance validation in the DB
	IF NOT EXISTS(SELECT 1 FROM transactions_ex.invoice WHERE invoice_id = v_invoice_id) THEN RAISE EXCEPTION 'Invoice % does not exist or it is already returned', v_invoice_id;
	ELSE RAISE NOTICE 'Invoice % exists and is active', v_invoice_id;
	END IF;

	SELECT product_id, amount INTO v_product_id, v_amount FROM transactions_ex.invoice_detail WHERE invoice_id = v_invoice_id;

--b. Increase the stock with the purchased amount
	UPDATE transactions_ex.products SET stock = stock + v_amount WHERE product_id = v_product_id;

--c. Update the invoice and mark as rturned
	UPDATE transactions_ex.invoice SET status = 'RETURNED' WHERE invoice_id = v_invoice_id;
	
COMMIT;
END $$ LANGUAGE plpgsql;