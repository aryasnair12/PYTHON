list_a=['apple','mango','grapes','banana']
print("list is",list_a)
count=0
for i in list_a:
    for j in i:
        if(j=='a'):
            count=count+1
print("the number of a in list is",count)