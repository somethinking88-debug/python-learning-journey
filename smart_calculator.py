number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

operation = input("Choose operation (+, -, *, /): ")

if operation == "+":
    print("Result:", number1 + number2)

elif operation == "-":
    print("Result:", number1 - number2)

elif operation == "*":
    print("Result:", number1 * number2)

elif operation == "/":
    if number2 != 0:
        print("Result:", number1 / number2)
    else:
        print("Cannot divide by zero!")

else:
    print("Invalid operation!")
