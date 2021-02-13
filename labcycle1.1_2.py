list=[]
n=int(input("enter the number of elements:"))
for i in range(0,n):
    list.append(int(input("enter the integer:")))
print("printing the positive integer:")
for i in list:
    if(i>0):
        print(i,end=" ")