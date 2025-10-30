create table if not exists lyfter_car_rental.users (
   user_id        serial primary key,
   full_name      varchar(50) not null,
   email          varchar(50) unique not null,
   username       varchar(50) unique not null,
   password       varchar(225) not null,
   birth_date     date not null,
   account_status boolean not null
)