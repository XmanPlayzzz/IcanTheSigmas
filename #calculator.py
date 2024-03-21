#calculator
num1 = input("Enter your first number")
num2 = input("Enter your second number")
operator = input("Enter the operator (+,-,*,/)")
if operator == '*':
    print(str(num1 * num2))
if operator == '+':
    print(str(num1 + num2))
elif operator == '-':
        print(num1 - num2)
elif operator == "/":
      if num2 == 0:
        print("The second number cannot be 0")
else:   
      print(str(num1 % num2))


