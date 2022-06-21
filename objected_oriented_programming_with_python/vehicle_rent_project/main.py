# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 14:18:35 2022

@author: ŞEVVAL
"""

from rent import bikeRent,carRent,customer

bike = bikeRent(100)
car = carRent(10)
customer = customer()

main_menu = True

while True:
    
    if main_menu:
        print("""
              *****vehicle rental shop*****
              A letter is for Bike Menu
              B Letter is for Car Menu
              Q letter is for exit
              """)
        
        main_menu = False
        
        choice = input("enter a choice: ")
        
    if choice == "A" or choice == "a":
        
        print("""
              *****bike menu*****
              1. display available bikes
              2. request a bike on hourly basis $5 
              3. request a bike on daily basis $84
              4. return a bike 
              5. main menu
              6. exit
              """)
              
        choice = input("enter a choice: ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("it is not an integer value")
            continue
        
        if choice == 1:
            bike.displayStock()
            choice="A"
            
        elif choice == 2:
            customer.rentalTime_b = bike.rentHourly(customer.requestVehicle("bike"))
            customer.rentalBasis_b = 1
            main_menu = True
            print("-----------------")
            
        elif choice == 3:
            customer.rentalTime_b = bike.rentDaily(customer.requestVehicle("bike"))
            customer.rentalBasis_b = 2
            main_menu = True
            print("-----------------")
            
        elif choice == 4:
            customer.bill = bike.returnVehicle(customer.returnVehicle("bike"), "bike")
            customer.rentalBasis_b, customer.rentalTime_b, customer.bikes = 0,0,0
            main_menu = True
            
        elif choice == 5:
            main_menu = True
            
        elif choice == 6:
            break
        
        else:
            print("invalid input, please enter a number between 1-6")
            main_menu = True
            
    
    elif choice == "B" or choice == "b":
        
        print("""
              *****car menu*****
              1. display available car
              2. request a car on hourly basis $10 
              3. request a car on daily basis $192
              4. return a car 
              5. main menu
              6. exit
              """)
              
        choice = input("enter a choice: ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("it is not an integer value")
            continue
        
        if choice == 1:
            car.displayStock()
            choice="B"
            
        elif choice == 2:
            customer.rentalTime_c = car.rentHourly(customer.requestVehicle("car"))
            customer.rentalBasis_c = 1
            main_menu = True
            print("-----------------")
            
        elif choice == 3:
            customer.rentalTime_c = car.rentDaily(customer.requestVehicle("bike"))
            customer.rentalBasis_c = 2
            main_menu = True
            print("-----------------")
            
        elif choice == 4:
            customer.bill = car.returnVehicle(customer.returnVehicle("car"), "car")
            customer.rentalBasis_c, customer.rentalTime_c, customer.cars = 0,0,0
            main_menu = True
            
        elif choice == 5:
            main_menu = True
            
        elif choice == 6:
            break
        
        else:
            print("invalid input, please enter a number between 1-6") 
            main_menu = True
            
    
    elif choice == "Q" or choice == "q":
        break
    
    else:
        print("invalid input, please enter a,b,q")
        main_menu = True
        
    print("thank you for using rent a car shop")