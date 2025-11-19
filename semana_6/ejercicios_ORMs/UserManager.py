from sqlalchemy import insert, select,update, delete
from semana_6.ejercicios_ORMs.database_setup import engine, users_table

class UserManager:
    def __init__(self):
        self.engine = engine

    #Create User
    def create_user(self, name):
        stmt = insert(users_table).values(name=name)
        with engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()

    #Update user
    def update_user(self,user_id, new_name):
        stmt = (
            update(users_table)
            .where(users_table.c.id == user_id)
            .values(name=new_name)
        )
        with engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()

    #Delete user
    def delete_user(self, user_id):
        stmt = (
            delete(users_table)
            .where(users_table.c.id == user_id)
        )
        with engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()

    #Get all users 
    def get_all_users(self):
        stmt = select(users_table)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            return result.fetchall()
