str1=input("enter a string:")
dict1={}
key_s=dict1.keys()
for i in str1:
      if i in key_s:
          dict1[i]=dict1[i]+1
      else:
          dict1[i]=1
print(dict1)