from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column,Integer,String
from sqlalchemy import insert, select

metadata_obj = MetaData()

users_table = Table(
    "users",
    metadata_obj,
    Column("id",Integer, primary_key = True),
    Column("username",String(30)),
    Column("password",String(30)),
    Column("type",String(30))
)

class DB_Manager:
    def __init__(self):
        self.engine =create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
        metadata_obj.create_all(self.engine)

    def insert_user(self,username,password,type):
        stmt = insert(users_table).returning(users_table.c.id).values(username=username,password=password,type = type)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result.all()[0]  #explicacion en Notion
    
    def get_user(self,username,password,type):
        stmt = select(users_table).where(users_table.c.username==username).where(users_table.c.password==password)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            users = result.all()

            if (len(users)==0):
                return None
            else:
                return users[0]
            
    def get_user_by_id(self,id):
        stmt = select(users_table).where(users_table.c.id == id)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            users = result.all()
            if(len(users)==0):
                return None
            else:
                return users[0]



