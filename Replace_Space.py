def make_replace_space(s):
    a=""
    
    for i in range(0,len(s)):
        if s[i]==" ":
            a=a+"-"
        else:
            a=a+s[i]
            
    return a
name=input("Enter your full name:")
p=make_replace_space(name)
print("Hello Mr",p)