s=input("Enter a string: ")
l=len(s)
c=0
for i in range(l-1,-1,-1):
    if(s[c]!=s[i]):
        print("The string is not a palindrome")
        break
    c+=1
if(c==l):
    print("The string is a palindrome")