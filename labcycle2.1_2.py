nterms=int(input("how many number?"))
n1=0
n2=1
count=0
if nterms<=0:
    print("please enter a positive integer")
elif nterms==1:
    print("fibinocci series upto nterms:")
    print(n1)
else:
    print("fibinocci sequence:")
    while count<nterms:
      print(n1)
      nth=n1+n2
      n1=n2
      n2=nth
      count+=1