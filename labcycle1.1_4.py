list=[]
vowels=['a','e','i','o','u']
string=input("enter any word:")
for i in string:
    if((i in vowels)and(i not in list)):
        list.append(i)
print("vowels present in given word:",list)