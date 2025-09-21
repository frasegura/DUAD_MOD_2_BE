-- SQLite
DROP TABLE IF EXISTS cart_detail;
DROP TABLE IF EXISTS invoice_detail;
DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS shopping_cart;
DROP TABLE IF EXISTS invoice;
DROP TABLE IF EXISTS payment_method;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS users;

-- MAIN TABLES

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name VARCHAR(20),
    email VARCHAR(20) UNIQUE NOT NULL,
    register_date DATE
);


CREATE TABLE products (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	code VARCHAR(25) NOT NULL,
	name VARCHAR(25) NOT NULL,
	price INTEGER DEFAULT 0,
	admission_date DATE,
	brand VARCHAR(25)
);

CREATE TABLE payment_method(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	method_type VARCHAR(25) NOT NULL,
	bank_name VARCHAR(25),
	user_id INTEGER,
	FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE invoice(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	invoice_number INTEGER DEFAULT 0,
	purchase_date DATE,
	total_amount INTEGER DEFAULT 0,
	cx_phone_number VARCHAR(20),
	employee_code VARCHAR(20),

	--FK
	user_id INTEGER,
	pmnt_method_id INTEGER,
	FOREIGN KEY (user_id) REFERENCES users(id),
	FOREIGN KEY (pmnt_method_id) REFERENCES payment_method(id)
);

CREATE TABLE shopping_cart(
	id INTEGER PRIMARY KEY AUTOINCREMENT,	
	user_id INTEGER UNIQUE, -- Foreign key 1:1
	FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE reviews(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	rev_comment VARCHAR(255),
	score SMALLINT DEFAULT 0,
	review_date DATE,
	--FK
	user_id INTEGER,
	product_id INTEGER,
	FOREIGN KEY (user_id) REFERENCES users(id),
	FOREIGN KEY (product_id) REFERENCES products(id)
);

-- JUNCTION  TABLES

CREATE TABLE invoice_detail(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	quantity SMALLINT DEFAULT 0,
	subtotal INTEGER DEFAULT 0,

	invoice_id INTEGER,
	product_id INTEGER,
	FOREIGN KEY (invoice_id) REFERENCES invoice(id),
    FOREIGN KEY (product_id) REFERENCES products(id)

);

CREATE TABLE cart_detail(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	user_email VARCHAR(25),
	quantity SMALLINT DEFAULT 0,

	shopping_cart_id INTEGER,
	product_id INTEGER,
	FOREIGN KEY (shopping_cart_id) REFERENCES shopping_cart(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);