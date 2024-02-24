#A python program for banking system using class,methods,atributes and objects
#import time will help in updating the current time as an opening date of your bank
import datetime
#creating the class called account and then inisialize the atributes for our program
class BankAccount:
    def __init__(self,account_number,balance,customer_name):
        self.account_number=account_number
        self.balance=balance
        self.date_of_openning=datetime.date.today()
        self.customer_name=customer_name
#creating a method called deposit and pass the conditon using if....else.. statements        
    def deposit(self,amount) :
        if amount > 0:
            self.balance +=amount

            return amount
        else:
            print("invalid deposit amount")
            return None
 #creating a method called withdraw and pass the conditions using if...else... statements           
    def withdraw(self,amount) :
        if amount <0:
            print("invalid input!!!")
            return None
        elif amount > self.balance:
            print("insufficient balance")
            return None
        else:
            self.balance -=amount
            return amount
#creating a function called check_balance that will return the users current balance
        
    def check_balance(self) :
        print("current balance: KSH.{:.2f}".format(self.balance))

#creating a function called customer_detail that will return the customer name,balance,openingdate and the account number
        
    def customer_details(self):
        print("customer name: {}".format(self.customer_name))
        print("account number: {}".format(self.account_number))
        print("date of account openning: {}".format(self.date_of_openning))
        print("current balance: {:.2f}".format(self.balance))
#prompt the user to enter the account number,balance and customer name
        
account_number=input("Enter your account number: ")
balance=int(input("Enter your balance: "))
customer_name=input("Enter your Name: ")

#creating an object called myBank and pas the parameter fom the class BankAccount   
myBank = BankAccount( account_number, balance, customer_name)
myBank.deposit(int(input("Enter the amount you want to deposit: ")))
myBank.withdraw(int(input("Enter the amount you want to withdraw: ")))
myBank.check_balance()
myBank.customer_details()
    
      
