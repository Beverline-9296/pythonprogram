#a python program to calculate the temperature both in celcius ad fehreheight
#create a class called Temperature and initialize the atributes
class Tempereture:
    def __init__(self,celsius,fehreheight):
        self.celsius=celsius
        self.fehreheight=fehreheight
#create a method name convert_to_fehren        
    def convert_to_fehren(self):
        f=self.celsius*1.8+32
        print("Enter the temperature in celsius:",celsius)
        return f 
#create a method convert_to_cel  
    def convert_to_cel(self):
        c=self.fehreheight/1.8-32
        print("Enter the temperature in fahreheight",fahreheight)
        return c 
#Prompt the user to enter the input
celsius=float(input("enter the celcius to be convered: ")) 
fahreheight=float(input("enter the fehreheight to be convered: "))
#create a object called temp
temp=Tempereture(celsius,fahreheight) 
#print the output  
temp.convert_to_cel()
temp.convert_to_fehren()
