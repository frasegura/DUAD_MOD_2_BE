from flask import Flask, request, jsonify, Response
from db import DB_Manager
from jwt_manager import JWT_Manager

app = Flask("user-service")

db_manager = DB_Manager()
jwt_manager = JWT_Manager()

@app.route("/register",methods = ["POST"])
def user_register():
    data = request.json

    if(data.get("username")==None or data.get("password") == None ):
        return jsonify({"Error":"Missing fields"}),400
    else:
        result = db_manager.insert_user(data.get("username"), data.get("password"))
        user_id = result[0]

        token = jwt_manager.encode({"id": user_id})
        return jsonify(token = token)
    
@app.login("/login" , methods = ["POST"])
def login():
    data = request.json

    if(data.get("username")==None or data.get("password")==None):
        return jsonify({"Error":"Missing fields"}),400
    else:
        result = db_manager.get_user(data.get_user("username"), data.get_user("password"))

        if(result == None):
            return jsonify({"Msg":"No user found"}),400
        else:
            user_id = result[0]
            token = jwt_manager.encode({"id":user_id})
            return token
        
@app.login("/me", methods = ["GET"])
def me():
    




if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug= True)