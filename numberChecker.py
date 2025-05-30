userinput = input("Please give a number either positive or negative: ")
userinput = int(userinput)
if userinput > 0:
    print("Your given number is POSITIVE")
elif userinput < 0:
    print("Your given number is NEGATIVE")
else:
    print("You entered ZERO")