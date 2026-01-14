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
            
            


    

    
    


