from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String,ForeignKey

metadata_obj = MetaData()

# DB declaration : tables for users, directions and cars

users_table = Table(
    "users",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name",String(30))
)

addresses_table = Table(
    "addresses",
    metadata_obj,
    Column("id",Integer, primary_key=True),
    Column("street", String(100)),

    # FK
    Column("user_id",Integer,ForeignKey("users.id"),nullable=False)
)

cars_table = Table(

    "cars",
    metadata_obj,
    Column("id",Integer, primary_key=True),
    Column("model",String(50)),

    #FK
    Column("user_id",Integer, ForeignKey("users.id"), nullable=True)
)


#Create connection
DB_URI = 'postgresql://postgres:postgres@localhost:5432/postgres'
engine = create_engine(DB_URI, echo= False)

try:
    connection = engine.connect()
    print("Connection successfull")
    connection.close()
except Exception as e:
    print("Connection failed :", e) 


#Table validation: tables will be created if they do not exist. 

metadata_obj.create_all(engine)
print("Tables are validated, and created if they do not exist.")

