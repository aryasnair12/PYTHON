list1=[]
n=int(input("enter no: of element in list1"))
for x in range(0,n):
    list1.append(int(input("enter list item")))
print(list1)
total=0
for x in list1:
    total=total+x
print("sum of list is:",total)