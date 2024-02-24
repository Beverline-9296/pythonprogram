#A python program to calculate the area and perimeter of a rectangle
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
         area=self.length*self.width
         return area
    def perimeter(self):
        perimeter=2 * (self.length + self.width) 
        return perimeter
#prompt the user to enter the length and width    
length=int(input("enter the length:"))     
width=int(input("enter the width:")) 
#creating an object name rectangle1   
rectangle1=Rectangle(length,width)
#Print the output
print("The area is: ",rectangle1.area())  
print("The perimeter is:",rectangle1.perimeter()) 
