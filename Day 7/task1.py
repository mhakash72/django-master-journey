try:
    input1 = int(input("Enter first number : "))
    input2 = int(input("Enter second number : "))
    div = input1/input2
except ZeroDivisionError:
     print("Cannot divide by zero!")