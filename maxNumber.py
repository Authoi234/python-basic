n1 = int(input("Please enter a number: "))
n2 = int(input("Please enter another number: "))
n3 = int(input("Please enter last number: "))

if n1 > n2:
    max_n = n1
else:
    max_n = n2
if (n3>max_n):
    max_n = n3
print("Maximum/Highest Number is : ", max_n)