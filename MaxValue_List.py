li = list()
n=int(input("Enter how many number you want to store:"))
for i in range(0,n):
    print("Enter the ",i+1," th  value:")
    value=int(input())
    li.append(value)
print("The list is:",li)
big = li[0]
for i in range(1,n):
    if(li[i]>big):
        big=li[i]
print("The largest value is:",big)