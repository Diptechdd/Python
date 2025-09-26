password =input("Enter a Password: ")
l=len(password)

c=0
c1=0
c2=0
for i in password:
    x=ord(i)        
    if (x>=65 and x<=90):
        c+=1    
    elif (x>=97 and x<=122):
        c1+=1
    elif (str.isdigit(i)):
        c2+=1

if (l<8 ):
    print("Entered password is not of 8 charecters")
elif (c==0 ):
    print("Entered password does not contain an uppercase letter")
elif (c1==0 ):  
    print("Entered password does not contain a lowercase letter")
elif (c2==0 ):
    print("Entered password does not contain a digit")
else:
    print("Valid Password")