def Execution(list1):
    sum=0
    for i in list1:
        sum=sum+i**3
    return sum
def main(list1):
    return Execution(list1)

list1=[int(x) for x in input("Enter the numbers in the list separated by space: ").split()]
print("The sum of cubes of all the numbers in the list is: ",main(list1 ))