list_a=[11,2,7,8,10,15,6]
print("list is:",list_a)
new_list=[]
for i in list_a:
    if(i%2==0):
        i=i+1
    else:
        new_list.append(i)
print("new list is:",new_list)