
-- Obtenga todos los libros y sus autores
SELECT b.name AS book_name,
        a.name AS author_name
FROM books as b
INNER JOIN authors as a
    ON b.author_id = a.id

--Obtenga todos los libros que no tienen autor

SELECT b.name AS book_name,
        a.name AS author_name
FROM books as b
LEFT JOIN authors as a
    ON b.author_id = a.id
WHERE a.id IS NULL


--Obtenga todos los autores que no tienen libros

SELECT b.name AS book_name,
        a.name AS author_name
FROM authors as A
LEFT JOIN books as b
    ON a.id = b.author_id
WHERE b.id IS NULL

-- Obtenga todos los libros que han sido rentados en algún momento

SELECT DISTINCT b.name AS book_name
FROM rents AS r
INNER JOIN books as b
    ON r.books_id = b.id


-- Obtenga todos los libros que nunca han sido rentados

SELECT b.name as book_name
FROM books as b
LEFT JOIN rents as r
    ON b.id = r.books_id
WHERE r.books_id IS NULL

-- Obtenga todos los clientes que nunca han rentado un libro

SELECT c.name as customer_name
FROM customers as c
LEFT JOIN rents as r
    ON c.id = r.customer_id
WHERE r.customer_id IS NULL

-- Obtenga todos los libros que han sido rentados y están en estado “Overdue”

SELECT b.name as book_name 
FROM books AS b
INNER JOIN rents AS r 
    ON b.id = r.books_id
WHERE r.state = "Overdue"