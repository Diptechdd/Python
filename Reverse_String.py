def reverse_string(s):
     n=len(s)
     j=0
     p=""
     for i in range(n-1,-1,-1):
          p=p+s[i];
          
     return p
         
s=input("Enter a string: ")
print("The input string is:", s)
print("The reverse string is: ",reverse_string(s))

'''print(s[i],end="")'''