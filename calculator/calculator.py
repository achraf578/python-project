def add(*numbers):
    total=0

    for number in numbers:
        total+=number

    return total

def sub(*numbers):
    total=0

    for number in numbers:
        total-=number

    return total

def mult(*numbers):
    total=1

    for number in numbers:
        total*=number

    return total

def div(*numbers):
    total=numbers[0]

    for number in numbers[1:]:
        total/=number
    
    return total


