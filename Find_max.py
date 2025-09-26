def main():
    x=int(input("Enter first number: "))
    y=int(input("Enter second number: "))
    z=int(input("Enter third number: "))   
    return x,y,z
def find_max(n1,n2,n3):
    if(n1>=n2 and n1>=n3):
        return n1
    elif (n2>=n1 and n2>=n3):
        return n2
    else:
        return n3
a,b,c=main()
p=find_max(a,b,c)
print("The big number among three is: ",p)