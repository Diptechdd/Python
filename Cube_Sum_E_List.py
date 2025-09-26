def main(li):
    sum=0
    n=len(li)
    for i in range(n):
        sum=sum+li[i]**3
    return sum
p=int(input("Enter number of element of the list:"))
list1=[]
for i in range(p):
    print("Enter ",i+1,"th value of the list:")
    list1.append(int(input(""))) 
print("the original list is:",list1)
print("Sum of Cube of eachelement of the list is:",main(list1))