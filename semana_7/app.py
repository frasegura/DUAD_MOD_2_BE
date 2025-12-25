from flask import Flask, request, jsonify, Response
from db import DB_Manager
from jwt_manager import JWT_Manager

app = Flask("user-service")

db_manager = DB_Manager()
jwt_manager = JWT_Manager("Shiro", 'HS256')


@app.route("/test" , methods =["GET"])
def test():
    return "<p>Hello worlds</p>"

@app.route("/register",methods = ["POST"])
def user_register():
    data = request.json

    if(data.get("username")== None or data.get("password") == None or data.get("role") == None):
        return jsonify({"Error":"Missing fields"}),400
    else:
        result = db_manager.insert_user(data.get("username"), data.get("password"), data.get("role"))
        user_id = result[0]

        token = jwt_manager.encode({"id": user_id})
        return jsonify(token = token)
    
@app.route("/login" , methods = ["POST"])
def login():
    data = request.json

    if(data.get("username")==None or data.get("password")==None or data.get("role")==None):
        return jsonify({"Error":"Missing fields"}),400
    else:
        result = db_manager.get_user(data.get("username"), data.get("password"), data.get("role"))

        if(result == None):
            return jsonify({"Msg":"No user found"}),400
        else:
            user_id = result[0]
            token = jwt_manager.encode({"id":user_id})
            return token
        
@app.route("/me", methods = ["GET"])
def me():
    try:
        token = request.headers.get("Authorization")
        if (token is not None):
            token = token.replace("Bearer ", "")
            decoded = jwt_manager.decode(token)
            user_id = decoded["id"]
            user = db_manager.get_user_by_id(user_id)
            return jsonify(id= user_id, username = user[1], role = user[3])
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


#CRUD para productos:

@app.route("/products" , methods = ["POST"])
def create_product():
    user = get_current_user()
    # print("USER:", user)
    # print("ROLE:", user[3])

    if user is None or not is_admin(user):
        return Response(status=403)
    
    data = request.json

    product_id = db_manager.insert_products(data.get("name"),data.get("price"),data.get("entry_date"),data.get("quantity"))
    return jsonify({"product_id" : product_id}),200

@app.route("/products" , methods = ["GET"])
def get_products():
    products = db_manager.get_all_products()

    result = []
    for p in products:
        result.append({
            "id": p.id,
            "name":p.name,
            "price":p.price,
            "entry_date":str(p.entry_date),
            "quantity": p.quantity
        })

    return jsonify(result),200

@app.route("/products/<int:product_id>" , methods = ["GET"])
def get_product_by_id(product_id):
    product = db_manager.get_products_by_id(product_id)

    if product is None:
        return jsonify({"error":"Product not found"}),400
    
    return jsonify({
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "entry_date":str(product.entry_date),
        "quantity": product.quantity
    })

@app.route("/products/<int:product_id>", methods = ["PUT"])
def update_product(product_id):
    user = get_current_user()

    if user is None or not is_admin(user):
        return Response(status=403)
    
    data = request.json

    db_manager.update_products(
        product_id,
        data["name"],
        data["price"],
        data["entry_date"],
        data["quantity"]
    )

    return jsonify({"Msg":"Product updated"})

@app.route("/products/<int:product_id>" , methods = ["DELETE"])
def delete_product(product_id):
    user = get_current_user()

    if user is None or not is_admin(user):
        return Response(status=403)
    
    db_manager.delete_products(product_id)
    return jsonify({"Msg":"Product deleted"})

@app.route("/buy", methods =["POST"])
def buy_product():
    user = get_current_user()

    if user is None:
        return Response(status=403)
    
    data = request.json

    try:
        invoice_id = db_manager.create_invoice(
            user_id =user[0],
            items=data["items"]
        )

        return jsonify({
            "Msg":"Purchase succesful",
            "invoice_id" : invoice_id
        }),201
    
    except Exception as e:
        return jsonify({"error":str(e)}),400
    

@app.route("/invoices/<int:invoice_id>" , methods = ["GET"])
def get_invoice_detail(invoice_id):
    user = get_current_user()

    if user is None:
        return Response(status=403)
    
    details = db_manager.get_invoice_details(invoice_id)

    if len(details) == 0:
        return jsonify({"error":"Invoice not found"}),400
    
    invoice_owner = db_manager.get_invoice_by_id(invoice_id)

    if not is_admin(user) and invoice_owner.user_id != user[0]:
        return Response(status=403)
    
    
    invoice_info = {
        "invoice_id": details[0].id,
        "date": str(details[0].date),
        "total": details[0].total_amount,
        "items": []
    }

    for det in details:
        invoice_info["items"].append({
            "product_id": det.product_id,
            "product_name": det.product_name,
            "quantity": det.quantity,
            "subtotal": det.subtotal
        })

    return jsonify(invoice_info)





if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug= True)




#token admin: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTR9.v--HgrBSfeiQ7-NPpwdYK47ggApd3N9jGRg5H5lTv5g"
#token user: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTB9._vRUJDS_3-Zq4FZaZQ1csG2UlpgSb8d8SIcmsVby-BA"
