import  sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, jsonify
from DB.cars import CarRepository
from DB.users import UserRepository
from DB.rents import RentRepository
from connection import PgManager

db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="postgres",
    host="localhost"
)



app = Flask(__name__)

user_repo = UserRepository(db_manager)
car_repo = CarRepository(db_manager)
rent_repo = RentRepository(db_manager)

#CREATE----------------

#Create users
@app.route('/users' , methods =['POST'])
def create_user():
    data = request.json
    result = user_repo.create(data)
    return jsonify({"message":"User created", "user" : result}),201

#Create cars
@app.route('/cars', methods = ["POST"])
def create_cars():
    data = request.json
    result = car_repo.create(data)
    return jsonify({"message":"Car created", "car" : result}),201

#Create rents
@app.route('/rentals' , methods =['POST'])
def create_rental():
    data= request.json
    result = rent_repo.create_rental(data)
    return jsonify({"message":"Rent created", "rental" : result}),201

#UPDATE------------------

#Update car status
@app.route('/cars/<int:car_id>/is_available', methods = ['PUT'])
def update_car_status(car_id):
    data = request.json
    status = data.get("is_available")
    result =car_repo.update_car_status(car_id,status)
    return jsonify ({"message":"Car status updated", "result" : result}),201


#Update user status
@app.route('/users/<int:user_id>/account_status', methods = ["PUT"])
def update_user_status(user_id):
    data = request.json
    status = data.get("account_status")
    result = user_repo.update_status(user_id,status)
    return jsonify({"message":"User status update","result": result}),201

#Complete a rent 
@app.route('/rentals/<int:rental_id>/complete',  methods = ["PUT"])
def complete_rental(rental_id):
    result  = rent_repo.confirm_return(rental_id)
    return jsonify({"message":"Rental status updated to completed", "result":result})

#Change rental status

@app.route('/rentals/<int:rental_id>/status', methods = ["PUT"])
def change_rental_status(rental_id):
    data = request.json
    status = data.get("status")
    result = rent_repo.update_rental_status(rental_id,status)
    return jsonify({"message":"rental status updated", "result":result})

#Flag user as defaulter

@app.route('/users/<int:user_id>/status', methods =["PUT"])
def flag_user(user_id):
    data = request.json
    status = data.get("status")
    result = user_repo.flag_user(user_id,status)
    return jsonify({"message":"Flag status updated", "result":result})

#List------------------------

#List all users:

@app.route('/users', methods = ["GET"])
def list_users():
    filters = request.args.to_dict()
    result = user_repo.get_users(filters)
    return jsonify(result)

#List all cars
@app.route('/cars', methods=["GET"])
def list_cars():
    filters = request.args.to_dict()
    result = car_repo.get_cars(filters)
    return jsonify(result)

#List all rentals

@app.route('/rentals', methods = ["GET"])
def list_rentals():
    filters = request.args.to_dict()
    result  = rent_repo.get_rentals(filters)
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="localhost",port=8000,debug=True)
