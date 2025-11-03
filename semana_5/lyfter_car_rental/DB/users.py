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
            "account_status": user_record[6],
            "is_flagged":user_record[7]
        }
    
    #Basic tests for DB

    def get_users(self, filters=None):
        try:
            base_query = "SELECT * FROM lyfter_car_rental.users"
            params = []

            if filters:
                conditions = []
                for key, value in filters.items():
                    conditions.append(f"{key} = %s")
                    params.append(value)
                base_query += " WHERE " + " AND ".join(conditions)

            results = self.db_manager.execute_query(base_query, tuple(params))
            return [self._format_user(result) for result in results]
        except Exception as e:
            print("Error:", e)
            return False

    def create(self,user_data):
        try:
            self.db_manager.execute_query("INSERT INTO lyfter_car_rental.users(full_name,email,username,password,birth_date,account_status,is_flagged) VALUES (%s,%s,%s,%s,%s,%s,%s)",(
                user_data["full_name"],
                user_data["email"],
                user_data["username"],
                user_data["password"],
                user_data["birth_date"],
                user_data["account_status"],
                user_data["is_flagged"]
            ))
            print("User inserted successfully")
            return True
        except Exception as error:
            print("An error has ocurred while  inserting a user", error)
            return False
        
    def update_status(self,user_id,new_status):
        try:
            self.db_manager.execute_query("UPDATE lyfter_car_rental.users SET account_status  = %s WHERE user_id = %s", (new_status, user_id,))
            print(f"User ID {user_id} status updated to {new_status}")
            return True
        except Exception as e:
            print("An error ocurred while updating the status of the user", e)
            return False
        
    def flag_user(self,user_id, flagged):
        try:
            user = self.db_manager.execute_query("SELECT user_id, username, is_flagged FROM lyfter_car_rental.users WHERE user_id = %s",(user_id,))
            if not user:
                print(f"No user found with the ID {user_id}")
                return False
            if user[0][2] is True:
                print(f"The user {user_id} is already flagged as debtor")
                return False
                
            self.db_manager.execute_query("UPDATE lyfter_car_rental.users SET is_flagged = %s WHERE user_id = %s",(flagged, user_id,))
            print("The flag status was updated ")
            return True
        except Exception as e:
            print("An error ocurred updating the flag status", e)
            return False
