from semana_6.ejercicios_ORMs.AddressManager import AddressManager
from semana_6.ejercicios_ORMs.CarManager import CarManager
from semana_6.ejercicios_ORMs.UserManager import UserManager

user_mngr = UserManager()
car_mngr = CarManager()
address_mngr =  AddressManager()




if __name__ == "__main__":

    #--Users--:

    #Create users
    # user_mngr.create_user("Carlos")
    # user_mngr.create_user("Luis")

    # #Get users
    print(user_mngr.get_all_users())

    # #Update users
    # #updating user 1 (Fran to Franco)
    # user_mngr.update_user(1,"Franco")
    # print("User updated")
    # #get updated users
    # print(user_mngr.get_all_users())

    #Delete users

    # user_mngr.delete_user(1)
    # print(user_mngr.get_all_users())



    # #--Addresses--

    # #Create address
    # address_mngr.create_address("Calle Real",1)
    # address_mngr.create_address("Calle 123",1)
    # address_mngr.create_address("Calle Montes", 3)

    # #Get addresses
    print(address_mngr.get_all_address())

    # #Update address

    # address_mngr.update_address(1,"Calle actualizada 98745")
    # print(address_mngr.get_all_address())

    # #Delete address
    # address_mngr.delete_address(1)
    # print(address_mngr.get_all_address())

    # #--Cars--

    # #Create Cars
    # car_mngr.create_car("Toyota Yaris")
    # car_mngr.create_car("Honda CRV" , user_id= 1)

    # #Get Cars
    print(car_mngr.get_all_cars())

    # #Update Cars

    # car_mngr.update_car(1,"Toyota Yaris 2025")
    # print(car_mngr.get_all_cars())
    
    # #Delete Cars
    # car_mngr.delete_car(1)
    # print(f"Cars after deleting id :{1}",car_mngr.get_all_cars())

    # #Asign a car to a user:
    # car_mngr.assign_car_to_user(car_id=1,user_id=1)
    # print("Cars after asign car 1 to user 1 :",car_mngr.get_all_cars())
