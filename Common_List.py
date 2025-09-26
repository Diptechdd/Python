li1 = list()
n1=int(input("Enter length of list one:"))
for i in range(0,n1):
    print("Enter the ",i+1," th  value:")
    value=int(input())
    li1.append(value)
print("The list is:",li1)
li2 = list()
n2=int(input("Enter length of list 2:"))
for i in range(0,n2):
    print("Enter the ",i+1," th  value:")
    value=int(input())
    li2.append(value)
print("The list is:",li2)
if(n1>n2):
    l=n2
else:
    l=n1

li=list()
for i in range(n1):
    for j in range(n2):
        if(li1[i]==li2[j]):
            li.append(li1[i])
            break
            
print("The common elements in both list are:",li)
        