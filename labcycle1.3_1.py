def change(string):
    return string[-1:] + string[1:-1] + string[:1]
string=input("enter string:")
print("modified string")
print(change(string))