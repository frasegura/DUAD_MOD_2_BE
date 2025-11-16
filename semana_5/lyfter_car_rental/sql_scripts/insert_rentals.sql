insert into lyfter_car_rental.rentals (
   user_id,
   car_id.rental_date,
   rental_status
) values ( 1,
           5,
           now(),
           'ongoing' ),( 2,
                         3,
                         now(),
                         'completed' ),( 3,
                                         2,
                                         now(),
                                         'rented' ),( 4,
                                                      1,
                                                      now(),
                                                      'completed' );