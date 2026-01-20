from flask import Flask, request, jsonify, Response
from db_cach import DB_Manager
from jwt_manager_cach  import JWT_Manager



db_manager = DB_Manager()
jwt_manager = DB_Manager()


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


def prod_field_validation(name,price,entry_date,quantity):
    if not name or not price or not entry_date or not quantity:
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
        token = jwt_manager.encode({"id":result})
        return jsonify(token = token), 201
    
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
            token = jwt_manager.encode({"id":result})
            return token
    except KeyError as e:
        return jsonify({"Missing fields":e}), 400
    
@app.route("/me", methods =["GET"])
def me():
    try:
        token = request.headers.get("Authorization")
        if token is not None:
            token = token.replace("Bearer ", "")
            decoded = jwt_manager.decode(token)
            user_id = decoded["id"]
            user = db_manager.get_user_by_id(user_id)
            return jsonify(id= user_id, username = user[1], role = user[3]) # probar con respecto al return de la BD
        else:
            return Response(status=403)
        
    except Exception as e:
        return Response(status=500)

def get_current_user():
    token = request.headers.get("Authorization")
    if token is None:
        return None
    
    try:
        token = token.replace("Bearer ", "")
        decoded = jwt_manager.decode(token)
        user = db_manager.get_user_by_id(decoded["id"])
        return user
    except Exception as e:
        print("Error:", e)
        return None
    
def is_admin(user):
    return user[3] == "admin"


#**SEPARAR ENDPOINTS ***
#CRUD PARA PRODUCTOS **ACA VOY
@app.route("/products" , methods=["POST"])
def create_products():
    try:
        user = get_current_user()
        if user is None or not is_admin(user):
            return Response(status=403)

        data = request.json
        data_validation(data)

        product_name= data["name"]
        product_price = data["price"]
        product_entry_date = data["entry_date"]
        product_quantity = data["quantity"]
        prod_field_validation(product_name,product_price,product_entry_date,product_quantity)
        product_id = db_manager.insert_products()

        return jsonify({"Product added:":product_id})
    except Exception as e:
        return jsonify({"Error":e}),400

@app.route("/products", methods = ["GET"])
def get_products():
    try:
        products = db_manager.get_all_products()

        result = []
        for p in products:
            result.append({
                "id":p.id,
                "name":p.name,
                "price":p.price,
                "entry_date":str(p.entry_date),
                "quantity": p.quantity
            })
        return jsonify({result}),200
    except Exception as e:
        return jsonify({"Error":e}),400
    
@app.route("products/<int:product_id>" , methods =["GET"])
def get_products_by_id(product_id):
    try:
        product = db_manager.get_products_by_id(product_id)
        if product is None:
            return jsonify({"Error":"No product found"}),400
        result = {
            "id":product.id,
            "name":product.name,
            "price":product.price,
            "entry_date":str(product.entry_date),
            "quantity":product.quantity
        }
        return jsonify(result),200
    except Exception as e:
        return jsonify({"Error":e}),400


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
