d={'arya':60,'manju':50,'sona':55}
print("the dictionary is",d)
list_d=list(d.items())
print("the list is:",list_d)
list_d.sort()
print("dictionary in ascenting order:",list_d)
d1=list(d.items())
d1.sort(reverse=True)
print("dictionary in descenting order:",d1)
