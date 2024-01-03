class Rectangle:
  def __init__(self,width,length):
    self._length=length #private attribute
    self._width=width #private attribute
  def area(self):
    return self._length*self._width
  def __lt__(self,other):
    return self.area()< other.area()
print("first Rectangle")
length=int(input("enter the length of rectangle:"))
breadth=int(input("enter the breadth of rectangle:"))
s1=Rectangle(length,breadth)
print("area ofrectangle",s1.area())

print("second Rectangle")
length=int(input("enter the length of rectangle:"))
breadth=int(input("enter the breadth of rectangle:"))
s2=Rectangle(lenth,breadth)
print("area of rectangle",s2.area())
 
  def compare_area(self, other_rectangle):
    if self.area()>other_rectangle.area():
      print ("The first rectangle has a larger area")
    elif self.area()<other_rectangle.area():
      print ("The second rectangle has a larger area")
    else:
      print ("Both rectangles have the same area")
 
s1.compare_area(s2) 

