def swape_First_Last_char(s):
    a=""
    n=len(s)
    a=a+s[n-1]
    
    
    for i in range(1,n-1):
        a=a+s[i]
    a=a+s[0]   
            
    return a
name=input("Enter your full name:")
p=swape_First_Last_char(name)
print("",p)