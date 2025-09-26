li = list()
n=int(input("Enter how many number you want to store:"))
for i in range(0,n):
    print("Enter the ",i," th  value:")
    value=int(input())
    li.append(value)
print("The list is:",li)