# Making Faulty Calculator
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result

num1 = int(input("Enter a number : "))
num2 = int(input("Enter another number : "))
operator = input("Which operation you want to perform : ")
if operator == '+':
    if num1 == 56 and num2 == 9:
        print("Sum of these numbers =", 77)
    elif num1 == 9 and num2 == 56:
        print("Sum of these numbers =", 77)
    else :
        print("Sum of these numbers =", num1+num2)
elif operator == '-':
    print("Difference of these numbers =", num1-num2)
elif operator == '/':
    if num1 == 56 and num2 == 6:
        print("Division of these numbers =", 4)
    else :
        print("Division of these numbers =", num1/num2)
else:
    if num1 == 45 and num2 == 3:
        print("Multiplication of these numbers =", 555)
    elif num1 == 3 and num2 == 45:
        print("Multiplication of these numbers =", 555)
    else :
        print("Multiplication of these numbers =", num1*num2)