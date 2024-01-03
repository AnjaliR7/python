from graphics import rectangle,circle
from graphics.Threedgraphics import cuboid,sphere
#using rectangle module
length=int(input("Enter the length of rectangle:"))
width=int(input("enter the width of rectangle:"))
print ("area of a rectangle=",rectangle.area(length,width))
print("perimeter of the rectangle=",rectangle.perimeter(length,width))
#using circle module
radius=int(input("enter the radius of circle:"))
print("Area of the circle=",circle.area(radius))
print("perimeter of the circle=",circle.perimeter(radius))
#using cuboid module
length=int(input("Enter the length of cuboid:"))
width=int(input("enter the width of cuboid:"))
height=int(input("enter the height of cuboid:"))
print("surface area of the cuboid=",cuboid.surfacearea(length,width,height))
print("volume of the cuboid=",cuboid.volume(length,width,height))
#using sphere module
radius=int(input("enter the radius of sphere:"))
print("surface area of the sphere=",sphere.surfacearea(radius))
print("volume of the sphere=",sphere.volume(radius))
