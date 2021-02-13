list=[]
n=int(input("enter the number of elements:"))
for i in range(0,n):
    list.append(int(input("enter the number:")))
print("printing the square of numbers:")
for i in list:
    print(i*i,end=" ")