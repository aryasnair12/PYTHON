def hcf(a,b):
    if(b==0):
        return a
    else:
        return hcf(b,a%b)
a=26
b=118
print("gcd og 26 and 118:",end=" ")
print(hcf(26,118))