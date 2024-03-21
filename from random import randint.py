from random import randint
def bob():
    num1 = input("type your first number")
    num1 = int(num1)
    num2 = input("type your second number")
    num2 = int(num2)
    number_list = []
    for num in range(num1, num2, +1):  
        print(num)
bob()