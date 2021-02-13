def fun_ing(str1):
    if(len(str1)>=3):
        if(str1[-3:]=='ing'):
            str1=str1+"ly"
        else:
            str1=str1+"ing"
    print("modified string is",str1)
str=input("enter a string")
fun_ing(str)