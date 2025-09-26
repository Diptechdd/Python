def get_length(n):
    c=0
    for key in n:
        c+=1
    return c
s=input("Enter a string: ")
print("The string is ",s)
print("The length of the string is: ",get_length(s))