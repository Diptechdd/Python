def Count_Vowel():
    s=input("Enter a string: ")
    c=0
    j=0
    for i in s:
        if (s[j]=='a' or s[j]=='e' or s[j]=='i' or s[j]=='o' or s[j]=='u'):
            c+=1
            print(c," is vowel is ",i)
        
        elif(s[j]=='A' or s[j]=='E' or s[j]=='I' or s[j]=='O' or s[j]=='U'):
            c+=1
            print(c," is vowel is ",i)
        
        else:
           pass
        j+=1

    return s,c

q,p=Count_Vowel()
print("Number of vowel of the String is : ",p)