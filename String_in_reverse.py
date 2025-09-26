def make_reverse(s):
    a=""
    
    for i in range(len(s)-1,-1,-1):
        a=a+s[i]
            
    return a
name=input("Enter your full name:")
p=make_reverse(name)
print("reverse of ",name," is ",p)