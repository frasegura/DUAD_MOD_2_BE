create table if not exists lyfter_car_rental.cars (
   car_id serial primary key,
   brand  varchar(50) not null,
   model  varchar(50) not null,
   year   int not null,
   status boolean not null
);