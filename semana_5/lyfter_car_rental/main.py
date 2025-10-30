from connection import PgManager
from DB.users import UserRepository
from DB.cars import CarRepository
from DB.rents import RentRepository

db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="postgres",
    host="localhost"
)

users_repo = UserRepository(db_manager)
car_repo = CarRepository(db_manager)
rent_repo = RentRepository(db_manager)

#a. Add a new user 
# result = users_repo.create(
#     full_name="Francisco Segura",
#     email="fran.segura@example.com",
#     username = "fran12",
#     password="fran123",
#     birth_date="1997-04-18",
#     account_status=True
# )

#b. Add a new car 
# result_car =car_repo.create(
#     brand="Toyota",
#     model= "Yaris",
#     year="2025",
#     status= True
# )

#c. Change user status 
# users_repo.update_status(1,True)

#d. Change the car status
#car_repo.update_car_status(1,True)

#e. New rent with the user and car data
result_rent = rent_repo.create_rent(1,50,"ongoing")  #(user_id,car_id,rental_status)


db_manager.close_connection()