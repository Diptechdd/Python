def factorial(n):
    if n==1 :
        return 1
    else :
        return n * factorial(n-1)
    
x=int(input("Enter a number grater than 0: "))
print("Factorial of", x, "is", factorial(x))
    