from sqlalchemy import insert, update,select,delete
from semana_6.ejercicios_ORMs.database_setup import engine, cars_table

class CarManager:
    def __init__(self):
        self.engine = engine
    
    #CREATE
    def create_car(self,model, user_id = None):
        stmt = insert(cars_table).values(model = model, user_id = user_id)
        with engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()

    #UPDATE
    def update_car(self, car_id, new_model):
        stmt = (
            update(cars_table)
            .where(cars_table.c.id==car_id)
            .values(model= new_model)
        )
        with engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()

    #DELETE
    def delete_car(self, car_id):
        stmt =(
            delete(cars_table)
            .where(cars_table.c.id == car_id)          
        )
        with engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()

    #Get all cars
    def get_all_cars(self):
        stmt = select(cars_table)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            return result.fetchall()
    
    #Assign a car to a user
    def assign_car_to_user(self, car_id,user_id):
        stmt = (
            update(cars_table)
            .where(cars_table.c.id == car_id)
            .values(user_id=user_id)
        )

        with engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()

    