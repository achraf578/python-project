import calculator

num1=float(input("enter a number: "))
signe=input("enter a signe: ")
num2=float(input("enter a number: "))

if signe == "+":
    x=calculator.add(num1, num2)
elif signe == "-":
    x=calculator.sub(num1, num2)
elif signe == "*":
    x=calculator.mult(num1, num2)
elif signe == "/":
    try:
        x=calculator.div(num1, num2)
    except ZeroDivisionError:
        x=None
        print("that can't be done!")
else:
    x=None
    print("we don't do that here!")

if x != None:
    print(x)
else:
    exit
