string1='arya'
print("the orginal string is:"+str(string1))
a='$'
modify=string1[0]+string1[1:].replace(string1[0],a)
print("Replaced string:"+str(modify))