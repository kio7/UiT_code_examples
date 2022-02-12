# This program creates a Car object, a Truck object,
# and an SUV object.
import vehicles
import time
import pickle
from operator import attrgetter
import os

# Constants for the menu choices
NEW_CAR_CHOICE = 1
NEW_TRUCK_CHOICE = 2
NEW_SUV_CHOICE = 3
FIND_VEHICLE_CHOICE = 4
SHOW_VEHICLES_CHOICE = 5
QUIT_CHOICE = 6

def main():
    try:
        dir_name = os.path.dirname(__file__)
        vehicles_list = pickle.load(open(os.path.join(dir_name, "Vehicle_save_file.dat"), "rb"))
    except FileNotFoundError:
        user_input = str(input("The save file was not found, would you want us make a new one? Answer: ")).lower()
        if user_input == "yes":
            vehicles_list = []
            pickle.dump(vehicles_list, open(os.path.join(dir_name, "Vehicle_save_file.dat"), "wb"))
            vehicles_list = []

    choice = 0
    while choice != QUIT_CHOICE:
        # display the menu.
        display_menu()

        # Get the user's choice.
        try:
            choice = int(input('Enter your choice: '))
        except ValueError:
            print("Putting a string into this parameter doesn't work, try entering an Integer")
            
        # Perform the selected action.
        if choice == NEW_CAR_CHOICE:
            try:
                print('Input car data:')
                car_brand = str(input("Make: "))
                car_model_year = int(input("Year: "))
                car_milage = int(input("Milage: "))
                car_price = float(input("Price: "))
                car_doors = int(input("Doors: "))
                car = vehicles.Car(car_brand, car_model_year, car_milage, car_price, car_doors)
                vehicles_list.append(car)
            except ValueError:
                print("Sorry you entered an incorrect input, try again.")


        elif choice == NEW_TRUCK_CHOICE:
            try:    
                print('Input truck data:')
                truck_brand = str(input("Make: "))
                truck_model_year = int(input("Year: "))
                truck_milage = int(input("Milage: "))
                truck_price = float(input("Price: "))
                truck_wheel_drive = (input("Drive Type: "))
                truck = vehicles.Truck(truck_brand, truck_model_year, truck_milage, truck_price, truck_wheel_drive)
                vehicles_list.append(truck)
            except ValueError:
                print("Sorry you entered an inncorrect input, try again.")

        elif choice == NEW_SUV_CHOICE:
            try:
                print('Input SUV data:')
                suv_brand = str(input("Make: "))
                suv_model_year = int(input("Year: "))
                suv_milage = int(input("Milage: "))
                suv_price = float(input("Price: "))
                suv_passenger_capacity = int(input("Pass Cap: "))
                suv = vehicles.SUV(suv_brand, suv_model_year, suv_milage, suv_price, suv_passenger_capacity)
                vehicles_list.append(suv)
            except ValueError:
                print("Sorry you entered an inncorrect input, try again.")

        elif choice == FIND_VEHICLE_CHOICE:
            list_temp = []
            name_of_vehicle = (input("Name of Vehicle: ")).lower()
            for elem in vehicles_list:
                if name_of_vehicle in elem.brand.lower():
                    list_temp.append(elem)
            if list_temp:
                for elem in list_temp:
                    print(elem)
            else:
                print("No Vehicle with that name was found, returning to Main Menu.")
                

        elif choice == SHOW_VEHICLES_CHOICE:
            print('The following cars are in inventory:')
            for item in vehicles_list:
                print(item)

        elif choice == QUIT_CHOICE:
            vehicles_list = sorted(vehicles_list, key=attrgetter("brand"))
            pickle.dump(vehicles_list, open(os.path.join(dir_name, "Vehicle_save_file.dat"), "wb"))
            print('Exiting the program...')

        else:
            print('Error: invalid selection, try again.')
        time.sleep(1.5)   


# The display_menu function displays a menu.
def display_menu():
    print("="*20, end = '')
    print(' Menu ', end = '')
    print("="*20)
    print('1) New car')
    print('2) New truck')
    print('3) New SUV')
    print('4) Find vehicles by make')
    print('5) Show all vehicles')
    print('6) Quit')     
    print("="*46)

# Call the main function.
if __name__ == '__main__':
      main()
