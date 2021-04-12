class Time:
    def __init__(self,hour,minute,scnd):
        self.__h=hour
        self.__m=minute
        self.__s=scnd


    def __add__(self, other):
        return self.__h + other.__h,self.__m + other.__m,self.__s + other.__s



obj1=Time(2,45,13)
obj2=Time(1,30,5)
print(obj1+obj2)


