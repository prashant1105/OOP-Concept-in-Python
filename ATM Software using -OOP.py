#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 14:09:51 2019

@author: prashantpk
"""

class Atm:
    pin = ""
    _balance = 0       # "_" will hide the data from the programmer...
    amount = 0         # Instance Variable...
    counter = 1000     # Class Variable...
    
    """
    This is a class constructor that will be called whenever the object for the class Atm is created...
    """
    
    def __init__(self):    # Constructor for the class Atm...
        print("Hi! Welcome to our bank.")
        tempPin = input("Kindly enter a 4 digit number: ")
        if len(tempPin) == 4:
            self.pin = tempPin
            print("ATM Pin generated successfully.")
            self.customer_Id = Atm.counter + 1       # self.variable ----> is instance variable...
            Atm.counter = Atm.counter + 1            # class_name.variable  ----> is class variable...
            print("Your Customer ID is: ", self.customer_Id)
        else:
            print("Error!!! Please enter a 4 digit PIN.")
            
    def get_balance(self):
        
        """
        ===> Doc String of the FUNCTION: get_balance "
        This Function is used to return the current account balance for the user.
        Date: 25th June 2019
        Created By: Prashant Kumar
        """
        
        return self._balance    # Getter method which is used to hide the data as well as provide the data to the programmer indirectly... It creates a wrapper around the data...

    def set_balance(self, value):
        """
        ===> Doc String of the FUNCTION: set_balance "
        This Function is used to set the current account balance for the user.
        Date: 25th June 2019
        Created By: Prashant Kumar
        """
        
        if type(value) == int:
            self._balance = value
        else:
            print("Not Valid")   # To set the value of hidden variable by programmer...
                               
            
    def checkBalance(self):
        
        """
        ===> Doc String of the FUNCTION: check_balance "
        This Function is used to check the current account balance for the user.
        Date: 25th June 2019
        Created By: Prashant Kumar
        """
        
        temp = input("Kindly provide the PIN to proceed further: ")
        if temp == self.pin:
            print("Your correct balance is:  ", self.balance)
        else:
            print("Wrong PIN entered. Enter correct PIN.")
            
    def deposit(self):
        
        """
        ===> Doc String of the FUNCTION: deposit "
        This Function is used to deposit some amount to the account of the user.
        Date: 25th June 2019
        Created By: Prashant Kumar
        """
        
        temp = input("Kindly provide the PIN to proceed further: ")
        if temp == self.pin:
            self.amount = int(input("Enter the amount you want to deposit: "))
            self.balance = self.balance + self.amount
            #print(self.amount)
            print("Amount deposited successfuly")
        else:
            print("Wrong PIN entered. Enter correct PIN.")
            
    def withdrawl(self):
        
        """
        ===> Doc String of the FUNCTION: withdrawl "
        This Function is used to withdraw some amount from the account of the user.
        Date: 25th June 2019
        Created By: Prashant Kumar
        """
        
        temp = input("Kindly provide the PIN to proceed further: ")
        if temp == self.pin:
            amount = int(input("Enter the amount you want to withdraw: "))
            if amount <= self.balance:
                self.balance = self.balance - self.amount
                print("Amount successfuly withdrawn.")
            else:
                print("Low balance in account. Balance not withdrawn.")
        else:
            print("Wrong PIN entered. Enter correct PIN.")
            
    def changePin(self):
        
        """
        ===> Doc String of the FUNCTION: changePin 
        This Function is used to change the ATM Pin of the user.
        Date: 25th June 2019
        Created By: Prashant Kumar
        """
        
        temp = input("Kindly provide the PIN to proceed further: ")
        if temp == self.pin:
            new_pin = input("Enter the new PIN to change your PIN: ")
            if len(new_pin) == 4 and new_pin != self.pin:
                self.pin = new_pin
                print("ATM Pin changed successfully.")
            else:
                print("Error!!! Please enter a 4 digit PIN. Or you have entered the same PIN.")
        else:
            print("You have entered wrong PIN.")
            
            
obj = Atm()