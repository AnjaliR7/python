class Rectangle:
  def __init__(self,length,breadth):
    self.length=length
    self.breadth=breadth
  def area(self):
    return self.length*self.breadth
  def perimeter(self):
    return 2*(self.length+self.breadth)  
  def compare_area(self, other_rectangle):
   if self.area()>other_rectangle.area():
     print ("The first rectangle has a larger area")
   elif self.area()<other_rectangle.area():
     print ("The second rectangle has a larger area")
   else:
     print ("Both rectangles have the same area")
 
 
 

print("First rectangle") 
length=int(input("Enter the length of rectangle:"))
breadth=int(input("Enter the breadth of rectangle"))

s1=Rectangle(length,breadth) 

print("area of Rectangle1",s1.area())
print("perimeter of Rectangle1",s1.perimeter())

print("Second rectangle")
length=int(input("enter the length:"))
breadth=int(input("enter the breadth:"))

s2=Rectangle(length,breadth)

print("area of Rectangle2",s2.area())
print("perimeter of Rectangle2",s2.perimeter())

s1.compare_area(s2)
