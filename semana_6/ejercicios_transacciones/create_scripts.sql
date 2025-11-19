create table if not exists transactions_ex.users (
   user_id   serial primary key,
   full_name varchar(50) not null
)


create table if not exists transactions_ex.invoice (
   invoice_id   serial primary key,
   invoice_date date not null,
   user_id      int not null,
   foreign key ( user_id )
      references transactions_ex.users ( user_id )
)


create table if not exists transactions_ex.products (
   product_id   serial primary key,
   product_name varchar(50),
   price        int not null
)

create table if not exists transactions_ex.invoice_detail (
   invoice_detail_id serial primary key,
   amount            int,
   unit_price        int,
   total             int,
   invoice_id        int not null,
   product_id        int not null,
   foreign key ( invoice_id )
      references transactions_ex.invoice ( invoice_id ),
   foreign key ( product_id )
      references transactions_ex.products ( product_id )
)