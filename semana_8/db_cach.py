from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column,Integer,String, Date,Float, ForeignKey
from sqlalchemy import insert, select,update,delete
from datetime import datetime

metadata_obj = MetaData()

users_table = Table(
    "users",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username",String(50), unique=True),
    Column("password",String(200)),
    Column("role", String(30), default="user"),
    schema="cache_schema"
)

products_table =Table(
    "products",
    metadata_obj,
    Column("id", Integer, primary_key = True),
    Column("name",String(30)),
    Column("price", Float),
    Column("entry_date",Date),
    Column("quantity", Integer)
)

invoice_table = Table(
    "invoice",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer,ForeignKey("users.id")),
    Column("date", Date),
    Column("total_amount", Float)
)

invoice_detail_table = Table(
    "invoice_detail",
    metadata_obj,
    Column("id",Integer, primary_key=True),
    Column("invoice_id",Integer, ForeignKey("invoice.id")),
    Column("product_id",Integer, ForeignKey("products.id")),
    Column("quantity",Integer),
    Column("subtotal",Float)
)

class DB_Manager():
    def __init__(self):
        self.engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
        metadata_obj.create_all(self.engine)

    #USERS:
    def insert_user(self, username,password, role):
        stmt = insert(users_table).values(username=username,password=password, role=role).returning(users_table.c.id)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
            return result.scalar()
        
    def get_user(self,username,password,role):
        stmt = select(users_table).where(users_table.c.username==username).where(users_table.c.password==password).where(users_table.c.role==role)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            user = result.first()
            return user
        
    def get_user_by_id(self,user_id):
        stmt = select(users_table).where(users_table.c.id == user_id)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            user = result.all()
            if(len(user)==0):
                return None
            else:
                return user
            

    #PRODUCTS:

    #Ingresar productos
    def insert_products(self,name,price,entry_date,quantity):
        stmt = insert(products_table).values(name=name,price = price, entry_date = entry_date,quantity=quantity).returning(products_table.c.id)
        with self.engine.connect() as conn:
            products =conn.execute(stmt)
            conn.commit()
            return products.scalar()

    #Obtener todos los productos
    def get_all_products(self):
        stmt = select(products_table)
        with self.engine.connect() as conn:
            products = conn.execute(stmt)
            return products.all()
        
        if (len(products)==0):
            return None
        else:
            return products

    #Obtener productos por id
    def get_products_by_id(self, product_id):
        stmt = select(products_table).where(products_table.c.id == product_id)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            product = result.all()
            if(len(product)==0):
                return None
            else:
                return product[0]
    #Actualizar productos
    def update_products(self,product_id,name,price,entry_date,quantity):
        stmt = update(products_table).where(products_table.c.id == product_id).values(name=name,price=price,entry_date=entry_date,quantity=quantity)
        with self.engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()
        return True

    # Borrar productos
    def delete_products(self,product_id):
        stmt = delete(products_table).where(products_table.c.id==product_id)
        with self.engine.connect as conn:
            conn.execute(stmt)
            conn.commit()
        return True


    #INVOICES
    #Crear factura
    def create_invoice(self,user_id, items):
        with self.engine.connect() as conn:
            total = 0
            inv_details = []

            #verficiar que el producto exista
            for item in items:
                prod_id = item["product_id"]
                qty = item["quantity"]

                prod_smt = select(products_table).where(products_table.c.id==prod_id)
                product = conn.execute(prod_smt).first()

            if product is None:
                raise Exception("Product does not exists")
            elif  product.quantity < qty: #consultar
                return Exception("Product not available")
            
            subtotal = qty*product.price
            total += subtotal

            inv_details.append({
                "product_id":prod_id,
                "quantity": qty,
                "subtotal": subtotal
            })

            invoice_stmt = insert(invoice_table).returning(invoice_table.c.id).values(user_id=user_id, date = datetime.now(),total_amount=total)
            invoice = conn.execute(invoice_stmt)
            invoice_id = invoice.scalar()

            for detail in inv_details:
                detail_stmt = insert(invoice_detail_table).values(invoice_id = invoice_id,product_id = detail["product_id"],quantity= detail["quantity"],subtotal = detail["subtotal"])
                conn.execute(detail_stmt)

                stock_stmt = update(products_table).where(products_table.c.id == detail["product_id"]).values(quantity = products_table.c.quantity-detail["quantity"])
                conn.execute(stock_stmt)

            conn.commit()
            return invoice_id


    def get_invoice_by_user(self, user_id):
        stmt = select(invoice_table).where(invoice_table.c.id == user_id)
        with self.engine.connect() as conn:
            result  = conn.execute(stmt)
            return result.all()

    def get_invoice_details(self,invoice_id):
        stmt = select(invoice_detail_table).where(invoice_detail_table.c.invoice_id == invoice_id)
        with self.engine.connection() as conn:
            result = conn.execute(stmt)
            return result.all()
        
    def get_invoice_by_id(self,invoice_id):
        stmt = select(invoice_table).where(invoice_table.c.id == invoice_id)
        with self.engine.connection() as conn:
            result = conn.execute(stmt)
            return result.first()
            





            
            


    

    
    


