class Rectangle:

    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
        print("Rectangle is created")

    def area(self):
        return self.l*self.b
    def perimeter(self):
        return 2*(self.l+self.b)


obj1=Rectangle(8,5)
print("Area of rectangle is",obj1.area())
print("Perimeter of rectangle is",obj1.perimeter())

obj2=Rectangle(10,3)
print("Area of rectangle is",obj2.area())
print("Perimeter of rectangle is",obj2.perimeter())

if(obj1.area()>obj2.area()):
    print("Rectangle 1 is bigger")
else:
    print("Rectangle 2 is bigger")
