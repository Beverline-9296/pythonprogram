
#class python to calculate the area and circumfarence of a circle
#include the math method to help in declaraton of the math formular
import math
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
         area=math.pi*self.radius**2
         return area
    def perimeter(self):
        circum=math.pi*self.radius*2 
        return circum
#prompt the user to enter the radius of a circle
radius=int(input("enter the radius:"))
#create an object named circle1    
circle1=circle(radius)
print(f"The area of a circle with {radius} as a radius is:",circle1.area())  
print(f"The circumfarence of a circle with {radius} as a radius is:",circle1.perimeter())       


