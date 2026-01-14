from flask import Flask, request, jsonify, Response
from db_cach import DB_Manager



db_manager = DB_Manager()

app = Flask("user-service")

@app.route("/test" , methods=["GET"])
def test():
    return "<p>Hello world<p>"

#some validation functions:
def data_validation(data):
    if not data:
        return jsonify({"error": "Invalid JSON"}),400
    
def fields_validation(user_name,password,role):
    if not user_name or not password or not role:
            return jsonify({"error": "Fields cannot be empty"}),400

#CRUD PARA USUARIOS

@app.route("/register", methods = ["POST"])
def user_register():
    data = request.json
    data_validation(data)    
    #validaciones
    try:
        user_name = data["username"]
        password = data["password"]
        role = data["role"]

        fields_validation(user_name,password,role)
        
        #INSERTAR EN BD
        result = db_manager.insert_user(user_name,password,role)

        #AGREGAR TOKEN JWT
        return jsonify({"user_id": result}), 201
    
    except KeyError as e:
        return jsonify({"Missing fields":e}), 400
    

@app.route("/login", methods = ["POST"])
def login_user():
    data = request.json
    data_validation(data) 
    try:
        user_name = data["username"]
        password = data["password"]
        role = data["role"]

        fields_validation(user_name,password,role)
        ##Obtener el usuario de la BD
        result = db_manager.get_user(user_name,password,role)
        if result == None:
            return jsonify({"Message":"No user found"}),400
        else:
            return jsonify({"Message":"logged"}),200
        #AGREGAR TOKEN JWT
    except KeyError as e:
        return jsonify({"Missing fields":e}), 400



#CRUD PARA FRUTAS


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
