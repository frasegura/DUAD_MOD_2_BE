
create table books (
    id  INTEGER primary key AUTOINCREMENT,
    name varchar(25) not null,
    author_id INTEGER,
    foreign key ( author_id ) references authors ( id )
);

create table authors (
    id INTEGER primary key AUTOINCREMENT,
    name varchar(25) not null
);

create table customers (
    id INTEGER primary key AUTOINCREMENT,
    name  varchar(25) not null,
    email varchar(25)
);

create table rents (
    id INTEGER primary key AUTOINCREMENT,
    state  varchar(25) not null,
    books_id  INTEGER,
    customer_id INTEGER,
    foreign key ( books_id ) references books ( id ),
    foreign key ( customer_id ) references customers ( id )
);