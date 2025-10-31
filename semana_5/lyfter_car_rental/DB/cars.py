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

    #Basic tests for DB

    def  create(self,brand,model,year,is_available):
        try:
            self.db_manager.execute_query("INSERT INTO lyfter_car_rental.cars(brand,model,year,is_available) VALUES(%s,%s,%s,%s)" , (brand,model,year,is_available))
            print("Car inserted succesfully")
            return True
        except Exception as e:
            print("An error has ocurred while inserting a car", e)
            return False

    def update_car_status(self, car_id, new_status):
        try:
            self.db_manager.execute_query("UPDATE lyfter_car_rental.cars SET is_available = %s WHERE car_id = %s", (new_status, car_id))
            print(f"The {car_id} was successfully updated to  {new_status}")
            return True
        except Exception as e:
            print("An error has ocurred while upadting the car status")
            return False

    def get_rented_cars(self):
        try:
            results = self.db_manager.execute_query("SELECT car_id,brand,model,year,is_available FROM lyfter_car_rental.cars WHERE is_available = FALSE;")
            if not results:
                print("No rented cars found")
                return []
            
            formatted_result =  [self._format_cars(result) for result in results ]
            return formatted_result
        except Exception as e:
            print("An error ocurred while getting all the rented cars",e)
            return []

    def get_available_cars(self):
        try:
            results = self.db_manager.execute_query("SELECT car_id,brand,model,year,is_available FROM lyfter_car_rental.cars WHERE is_available = TRUE;")
            if not results:
                print("No available cars found")
                return []
            formatted_result = [self._format_cars(results) for result in results]
            return formatted_result
    
        except Exception as e:
            print("An error ocurred while all the available cars ",e )
            return []
