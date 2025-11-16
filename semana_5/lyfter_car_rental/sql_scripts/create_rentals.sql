create table if not exists lyfter_car_rental.rentals (
   rental_id     serial primary key,
   user_id       int not null,
   car_id        int not null,
   rental_date   timestamp default now(),
   rental_status varchar(20) default 'ongoing',
   foreign key ( user_id )
      references lyfter_car_rental.users ( user_id ),
   foreign key ( car_id )
      references lyfter_car_rental.cars ( car_id )
)