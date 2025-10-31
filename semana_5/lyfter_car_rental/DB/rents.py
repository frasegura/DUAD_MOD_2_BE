class RentRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def  _format_rent(self, rent_record):
        return {
            "rental_id": rent_record[0],
            "user_id":rent_record[1],
            "car_id": rent_record[2],
            "rental_date":rent_record[3],
            "rental_status": rent_record[4]
        }
    
    #Basic tests for DB

    def get_rental_by_id(self,rental_id):
        try:
            results  = self.db_manager.execute_query("SELECT rental_id,user_id, car_id, rental_date, rental_status FROM lyfter_car_rental.rentals WHERE rental_id = %s;",(rental_id,))
            formatted_results = [self._format_rent(result) for result in results]
            if not results:
                print(f"No rental found with the id :{rental_id}")
                return None
            return formatted_results[0]
        except Exception as e:
            print("An error has ocurred getting the rent id" , e)

    def confirm_return(self,rental_id):
        try:
            rental = self.get_rental_by_id(rental_id)
            if not rental:
                return False
            
            if rental["rental_status"] == "completed":
                print(f"Rental {rental_id} is already completed")
                return False
            
            update_rental_query = self.db_manager.execute_query("UPDATE lyfter_car_rental.rentals SET rental_status = 'completed' WHERE rental_id = %s;" , (rental_id,))
            update_car_query = self.db_manager.execute_query("UPDATE lyfter_car_rental.cars SET is_available = TRUE WHERE car_id = %s; ", (rental["car_id"],))

            print(f"Rental {rental_id} marked as completed and car {rental['car_id']} set to available.")
            return True

        except Exception as e:
            print("An error has ocurred during the confirmation: ", e)
            return False

    def disable_car_rental(self, rental_id):

        try:
            rental = self.get_rental_by_id(rental_id)
            if not rental:
                print(f"There's no rental for the selected ID : {rental_id} ")
                return False
            
            if rental["rental_status"] == "disabled":
                print(f"The rental for the car {rental['car_id']} is already disabled")
                return False
            
            update_rental_query = self.db_manager.execute_query("UPDATE lyfter_car_rental.rentals SET rental_status = 'disabled' WHERE rental_id = %s;", (rental_id,))
            update_car_query = self.db_manager.execute_query("UPDATE lyfter_car_rental.cars SET  is_available = False WHERE car_id=%s;", (rental['car_id'],))

            print(f"The car {rental['car_id']} was disabled to rent")
            return True 
        except Exception as e:
            print("Disabling failed", e)
            return False