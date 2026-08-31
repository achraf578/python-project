import calculator
start = True
while start is True:
    try:
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
                result = number1  # Keep the first number as the result if division by zero occurs
                print("Error: Division by zero is not allowed.")
        else:
            result = number1  # Default to the first number if the operator is invalid
            print("Invalid operator.")

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
                            result = result  # Keep the previous result if division by zero occurs
                            print("Error: Division by zero is not allowed.")
                    if result is not None:
                        print(f"Result: {result}")
                    else:
                        print("Invalid operation.")
            else:
                    print(f"Final Result: {result}")
                    print("Exiting the calculator.")
                    start=False
                    break
    except ValueError:
        print("Invalid input. Please enter a valid number.") 
