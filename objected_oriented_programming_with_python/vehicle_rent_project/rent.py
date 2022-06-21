# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 02:21:47 2022

@author: ŞEVVAL
"""

import datetime

#parent class
class vehicleRent():
    
    def __init__(self,stock):
        self.stock = stock #araçların stok durumu
        self.now = 0 #fatura(bill) hesaplanırken kaç saat kullanıldığını anlamak için kullanılacak.
    
    def displayStock(self):
        """
            display stock
        """
        print(" {} vehicle available to rent".format(self.stock))
        return self.stock
    
    def rentHourly(self,n): #n=araç sayısı
        """
            rent hourly
        """
        if n <= 0:
            print("number should be positive")
            return None
        
        elif n > self.stock:
            print("sorry {} vehicle available to rent".format(self.stock))
            return None
        
        else:
            self.now = datetime.datetime.now()
            print("rented a {} vehicle for hourly at {} hours".format(n,self.now.hour))
            
            self.stock -= n
            
            return self.now
    
    def rentDaily(self,n):
        """
            rent daily
        """
        if n <= 0:
            print("number should be positive")
            return None
        
        elif n > self.stock:
            print("sorry {} vehicle available to rent".format(self.stock))
            return None
        
        else:
            self.now = datetime.datetime.now()
            print("rented a {} vehicle for daily at {} hours".format(n,self.now.hour))
            
            self.stock -= n
            
            return self.now
    
    def returnVehicle(self, request, brand):
        """
            return a bill
        """
        car_h_price = 10
        car_d_price = car_h_price*8/10*24
        bike_h_price = 5
        bike_d_price = bike_h_price*7/10*24
        
        rentalTime, rentalBasis, numOfVehicle = request
        bill = 0
        
        if brand == "car":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime
                
                if rentalBasis == 1: #hourly
                    bill = rentalPeriod.seconds/3600*car_h_price*numOfVehicle
                    
                elif rentalBasis == 2: #daily
                    bill = rentalPeriod.seconds/(3600*24)*car_d_price*numOfVehicle
                    
                if (2 <= numOfVehicle):
                    print("you have extra 20% discount")
                    bill = bill * 0.8
                
                print("price:  ${} ".format(bill))
                return bill
                print("thank you for returning with your car")
                
            
            
        elif brand == "bike":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime
                
                if rentalBasis == 1: #hourly
                    bill = rentalPeriod.seconds/3600*bike_h_price*numOfVehicle
                    
                elif rentalBasis == 2: #daily
                    bill = rentalPeriod.seconds/(3600*24)*bike_d_price*numOfVehicle
                    
                if (4 <= numOfVehicle):
                    print("you have extra 20% discount")
                    bill = bill * 0.8
                
                print("price:  ${} ".format(bill))
                return bill
                print("thank you for returning with your bike")
                
            
        else:
            print("you don't rent a vehicle")
            return None
                
#child class 1

class carRent(vehicleRent):
    
    global discount_rate
    
    discount_rate = 15
    
    def __init__(self,stock):
        super().__init__(stock)
    
    def discount(self,b):
        """
            discount
        """
        bill = b - (b*discount_rate)/100
        return bill
    
#child class 2

class bikeRent(vehicleRent):
    
    def __init__(self,stock):
        super().__init__(stock)
    
#customer

class customer():
    
    def __init__(self):
        self.bikes = 0
        self.rentalBasis_b = 0
        self.rentalTime_b = 0
        self.cars = 0
        self.rentalBasis_c = 0
        self.rentalTime_c = 0
    
    
    def requestVehicle(self,brand):
        """
            take a request bike or car vehicle from customer
        """
        if brand == "bike":
            bikes = input("how many bikes would you like to rent?")
            
            try:
                bikes = int(bikes)
            except ValueError:
                print("you should write an integer value")
                return -1
            
            if bikes < 1:
                print("number of bikes should be greater than zero")
                return -1
            
            else:
                self.bikes = bikes
            return self.bikes
                
            
        elif brand == "car":
            cars = input("how many cars would you like to rent?")
            
            try:
                cars = int(cars)
            except ValueError:
                print("you should write an integer value")
                return -1
            
            if cars < 1:
                print("number of cars should be greater than zero")
                return -1
            
            else:
                self.cars = cars
            return self.cars
            
        else:
            print("request vehicle error")
    
    def returnVehicle(self,brand):
        """
            return bike or car vehicle
        """
        if brand == "bike":
            
            if self.rentalTime_b and self.rentalBasis_b and self.bikes:
                return self.rentalTime_b, self.rentalBasis_b, self.bikes
            else:
                return 0,0,0
                   
        elif brand == "car":
            
            if self.rentalTime_c and self.rentalBasis_c and self.cars:
                return self.rentalTime_c, self.rentalBasis_c, self.cars
            else:
                return 0,0,0
            
        else:
            print("vehicle error")