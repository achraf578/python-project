import calculator

num1=float(input("enter a number: "))
signe=input("enter a signe: ")
num2=float(input("enter a number: "))

if signe == "+":
    result=calculator.add(num1, num2)
elif signe == "-":
    result=calculator.sub(num1, num2)
elif signe == "*":
    result=calculator.mult(num1, num2)
elif signe == "/":
    try:
        result=calculator.div(num1, num2)
    except ZeroDivisionError:
        result=None
        print("that can't be done!")
else:
    result=None
    print("we don't do that here!")

if result != None:
    print(f"Result: {result}")
else:
    exit
