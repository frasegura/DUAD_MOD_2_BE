from sqlalchemy import insert, update, delete,select
from database_setup import engine , addresses_table

class AddressManager():
    def __init__(self):
        self.engine = engine

    def create_address(self,street, user_id):
        stmt = insert(addresses_table).values(street = street, user_id = user_id)
        with engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()

    def update_address(self,address_id, new_street):
        stmt = (
            update(addresses_table)
            .where(addresses_table.c.id==address_id)
            .values(street = new_street)
        )

        with engine.connect() as  conn:
            conn.execute(stmt)
            conn.commit()

    def delete_address(self, address_id):
        stmt = (
            delete(addresses_table)
            .where(addresses_table.c.id == address_id)
        )

        with engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()

    def get_all_address(self):
        stmt = select(addresses_table)
        with engine.connect() as conn: 
            result = conn.execute(stmt)
            return result.fetchall()


