def make_name_short(s):
    a=""
    a=a+s[0]
    a=a+". "
    for i in range(0,len(s)-1):
        if s[i]==" ":
            a=a+s[i+1]
            a=a+". "
            
    return a
name=input("Enter your full name:")
p=make_name_short(name)
print("Hello Mr",p)