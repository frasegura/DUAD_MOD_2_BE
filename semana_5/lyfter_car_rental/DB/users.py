class  UserRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_user(self, user_record):
        return{
            "user_id": user_record[0] ,
            "full_name":user_record[1],
            "username":user_record[2],
            "email": user_record[3],
            "password": user_record[4],
            "birth_date": user_record[5],
            "account_status": user_record[6]
        }
    
    #Basic tests for DB

    def create(self,full_name,email,username, password,birth_date,account_status):
        try:
            self.db_manager.execute_query("INSERT INTO lyfter_car_rental.users(full_name,email,username,password,birth_date,account_status) VALUES (%s,%s,%s,%s,%s,%s)",(full_name,email,username, password,birth_date,account_status))
            print("User inserted successfully")
            return True
        except Exception as error:
            print("An error has ocurred while  inserting a user", error)
            return False
        
    def update_status(self,user_id,new_status):
        try:
            self.db_manager.execute_query("UPDATE lyfter_car_rental.users SET account_status  = %s WHERE user_id = %s", (new_status, user_id))
            print(f"User ID {user_id} status updated to {new_status}")
            return True
        except Exception as e:
            print("An error ocurre while updating the status of the user", e)
            return False
