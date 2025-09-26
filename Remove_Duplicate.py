li = list()
n=int(input("Enter how many number you want to store:"))
for i in range(0,n):
    print("Enter the ",i+1," th  value:")
    value=int(input())
    li.append(value)
print("The list is:",li,len(li))
n1=len(li)
j=0
for i in range(0,len(li)-1):
    j=i+1
    while j<n1 :
        if(li[i]==li[j]):        
            li.remove(li[j])
            j=j-1 
            n1=n1-1
        print("i=",i, "j=",j)
        j+=1
          

        
print("The list after removing duplicate values is:",li)

