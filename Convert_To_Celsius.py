def convert_celsius(n):
    t=(n-32)*5 /9
    return t
x=float(input("Enter temparature in fahrenhite: "))
print("The temparature in Fahrenhite is: ",x,"*F")
print("The temparature in celsius is: ",convert_celsius(x),"*C")
