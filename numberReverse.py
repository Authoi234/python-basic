num = int(input("Please write a number, " ))
rev_num=0

while num>0:
    last_digit=num % 10
    rev_num, num = rev_num*10+last_digit, num // 10
print(rev_num)