def is_vowel(s):
    if (s=='a' or s=='e' or s=='i' or s=='o' or s=='u'):
        return True
    elif(s=='A' or s=='E' or s=='I' or s=='O' or s=='U'):
        return True
    else:
        return False
def main():
    s=input("Enter a string: ")
    c=0
    j=0
    for i in s:
        if (s[j]=='a' or s[j]=='e' or s[j]=='i' or s[j]=='o' or s[j]=='u'):
            c+=1
        
        elif(s[j]=='A' or s[j]=='E' or s[j]=='I' or s[j]=='O' or s[j]=='U'):
            c+=1
        
        else:
           pass
        j+=1

    return s,c
x=input("Enter a String:")
print(is_vowel(x))
c,p=main()
print("no of vowels in string ",c," is = ",p)


