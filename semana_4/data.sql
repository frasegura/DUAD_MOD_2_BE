
INSERT INTO authors (name)
    VALUES ('Miguel de Cervantes')
INSERT INTO authors (name)
    VALUES ('Dante Alighieri')
INSERT INTO authors (name)
    VALUES ('Takehiko Inoue')
INSERT INTO authors (name)
    VALUES ('Akira Toriyama')
INSERT INTO authors (name)
    VALUES ('Walt Disney')
----

INSERT INTO books (name,author_id)
    VALUES('Don Quijote',1)

INSERT INTO books (name,author_id)
    VALUES('La Divina Comedia',2)

INSERT INTO books (name,author_id)
    VALUES('Vagabond 1-3',3)

INSERT INTO books (name,author_id)
    VALUES('Dragon Ball 1',4)

INSERT INTO books (name,author_id)
    VALUES('The Book of the 5 Rings',NULL)

--

INSERT INTO customers(name,email)
    VALUES('John Doe','j.doe@email.com');

INSERT INTO customers(name,email)
    VALUES('Jane Doe','jane@doe.com');

INSERT INTO customers(name,email)
    VALUES('Luke Skywalker','darth.son@email.com');

--

INSERT INTO rents(books_id,customer_id,state)
    VALUES(1,2,'Returned');

INSERT INTO rents(books_id,customer_id,state)
    VALUES(2,2,'Returned');

INSERT INTO rents(books_id,customer_id,state)
    VALUES(1,1,'On time');

INSERT INTO rents(books_id,customer_id,state)
    VALUES(3,1,'On time');

INSERT INTO rents(books_id,customer_id,state)
    VALUES(2,2,'On time');
