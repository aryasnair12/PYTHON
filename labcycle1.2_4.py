list_a=[10,20,30,40]
list_b=[40,50,60,70]

length_a=len(list_a)
length_b=len(list_b)
if(length_b==length_a):
      print("list are of same length")
else:
      print("list are in different length")
s_a=sum(list_a)
s_b=sum(list_b)
if(s_b==s_a):
      print("sum is eqal")
else:
      print("sum not eqal")
op=any(check in list_b for check in list_a)
print("common value is",op)
