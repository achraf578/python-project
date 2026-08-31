import calculator

number1=float(input("Enter first number: "))
operator=input("Enter operator (+, -, *, /): ")
number2=float(input("Enter second number: "))

if operator == "+":
    result = calculator.add(number1, number2)
elif operator == "-":
    result = calculator.sub(number1, number2)
elif operator == "*":
    result = calculator.mult(number1, number2)
elif operator == "/":
    try:
        result = calculator.div(number1, number2)
    except ZeroDivisionError:
        result = None
        print("Error: Division by zero is not allowed.")

if result is not None:
    print(f"Result: {result}")
else:
    print("Invalid operation.")

while True:
    operator=input("Enter operator (+, -, *, /, =): ")
    if operator != '=':
        number=float(input("Enter number: "))
        if operator == "+":
            result = calculator.add(result, number)
        elif operator == "-":
            result = calculator.sub(result, number)
        elif operator == "*":
            result = calculator.mult(result, number)
        elif operator == "/":
            try:
                result = calculator.div(result, number)
            except ZeroDivisionError:
                result = None
                print("Error: Division by zero is not allowed.")
        if result is not None:
            print(f"Result: {result}")
        else:
            print("Invalid operation.")
    else:
        print(f"Final Result: {result}")
        print("Exiting the calculator.")
        break

 
