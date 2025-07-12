import math

def is_prime ( n ) :
  if n < 2:
    return False
  if n == 2:
    return True
  if n%2 == 0:
    return False
  m = math.sqrt(n)
  m = int(m) + 1
  for x in range(3, m, 2):
    if n % x == 0:
      return False
  return True

n1 = int(input("Pleaes write an number, " ))
n2 = int(input ("Please write another larger number, "))

prime_Numbers=[] 

for c in range(n1+1, n2):
  if is_prime(c) == True:
    prime_Numbers.append(c)

print(prime_Numbers)