new_list=[]
n=int(input("enter the number of element:"))
for i in range(0,n):
    element=int(input("enter number"))
    if element>100:
         new_list.append("over")
    else:
        new_list.append(element)
print(new_list)