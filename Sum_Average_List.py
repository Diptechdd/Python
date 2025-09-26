li = list()
n=int(input("Enter how many number you want to store:"))
for i in range(0,n):
    print("Enter the ",i+1," th  value:")
    value=int(input())
    li.append(value)
print("The list is:",li)
Sum = 0
for i in range(0,n):
    Sum = Sum + li[i]   
Average = Sum/n
print("The sum of the list is:",Sum)
print("The average of the list is:",Average)
