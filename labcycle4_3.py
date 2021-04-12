class Rectangle:
    def __init__(self,length,breadth):
        self.__l=length
        self.__b=breadth

    def area(self):
        return self.__l*self.__b

    def __lt__(self, other):
        return self.area() < other.area()

obj1=Rectangle(4,3)
obj2=Rectangle(5,6)

if(obj1<obj2):
    print("obj2 is bigger rectangle")
else:
    print("obj1 is bigger rectangle")
