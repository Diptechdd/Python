def Prime(n):
    '''check from 2 to n/2 also works  2 to sqrt(n) also works for 2 to n-1'''
    if n>1:
        for i in range(2,int(n/2)+1):   
            if (n%i)==0:
                return False
            else:
                return True
    else:
        return False
num=int(input("Enter a number: "))
if(Prime(num)): 
    print(num," is a Prime number") 
else:
    print(num," is not a Prime number") 
'''display all Prime numbers between 1 to 100'''
print("Prime numbers between 1 to 100 are: ")
for i in range(1,101):
    if(Prime(i)):
        print(i,end=" ")    
print()
'''display all Prime numbers between m to n'''
m=int(input("Enter the starting range: "))
n=int(input("Enter the ending range: "))
print("Prime numbers between",m," to ",n," are: ")
for i in range(m,n+1):
    if(Prime(i)):
        print(i,end=" ")
print()
'''display first n Prime numbers''' 
count=0
i=1
n=int(input("Enter how many Prime numbers you want to display: "))
print("First",n," Prime numbers are: ") 
while(count<n):
    if(Prime(i)):
        print(i,end=" ")
        count+=1
    i+=1
print()
'''display first m Prime numbers after n''' 
count=0
i=n+1
m=int(input("Enter how many Prime numbers you want to display after "+str(n)+": "))
print("First",m," Prime numbers after",n," are: ") 
while(count<m):
    if(Prime(i)):
        print(i,end=" ")
        count+=1
    i+=1        
print()
'''display first m Prime numbers before n'''
# count=0
# i=n-1   
# m=int(input("Enter how many Prime numbers you want to display before "+str(n)+": "))
# print("First",m," Prime numbers before",n," are: ") 
# while(count<m and i>1):
#     if(Prime(i)):
#         print(i,end=" ")
#         count+=1
#     i-=1
# print()
# '''display all Prime numbers between m to n'''
# m=int(input("Enter the starting range: "))  
# n=int(input("Enter the ending range: "))
# print("Prime numbers between",m," to ",n," are: ")
# for i in range(m,n+1):
#     if(Prime(i)):
#         print(i,end=" ")    
# print()
# '''display all Prime numbers between m to n in reverse order'''
# m=int(input("Enter the starting range: "))  
# n=int(input("Enter the ending range: "))
# print("Prime numbers between",m," to ",n," in reverse order are: ")
# for i in range(n,m-1,-1):
#     if(Prime(i)):
#         print(i,end=" ")
# print()
# '''display first n Prime numbers in reverse order'''
# count=0
# i=1000
# n=int(input("Enter how many Prime numbers you want to display in reverse order: "))
# print("First",n," Prime numbers in reverse order are: ")
# while(count<n and i>1):  
#     if(Prime(i)):
#         print(i,end=" ")
#         count+=1
#     i-=1    
# print()
