class CarRepository:
    def __init__(self,db_manager):
        self.db_manager = db_manager

    def _format_cars(self,car_record):
        return {
            "car_id": car_record[0],
            "brand":car_record[1],
            "model":car_record[2],
            "year":car_record[3],
            "status":car_record[4]
        }
    
    #CRUD

    def  create(self,brand,model,year,status):
        try:
            self.db_manager.execute_query("INSERT INTO lyfter_car_rental.cars(brand,model,year,status) VALUES(%s,%s,%s,%s)" , (brand,model,year,status))
            print("Car inserted succesfully")
            return True
        except Exception as e:
            print("An error has ocurred while inserting a car", e)
            return False
        
    def update_car_status(self, car_id, new_status):
        try:
            self.db_manager.execute_query("UPDATE lyfter_car_rental.cars SET status = %s WHERE car_id = %s", (new_status, car_id))
            print(f"The {car_id} was successfully updated to  {new_status}")
            return True
        except Exception as e:
            print("An error has ocurred while upadting the car status")
            return False
        
    

    