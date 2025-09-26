def swap(s, i, j):
    s[i], s[j] = s[j], s[i]  # swap elements

myname = input("Enter the string: ")

# convert string to list (mutable)
chars = list(myname)

i, j = 0, len(chars) - 1
while i < j:
    swap(chars, i, j)
    i += 1
    j -= 1

# join list back to string
reversed_name = "".join(chars)
print(reversed_name)