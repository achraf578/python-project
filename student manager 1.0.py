students = [
    {"name": "Omar", "grades": [15, 17, 12]},
    {"name": "Yasser", "grades": [8, 11, 7]},
    {"name": "Ali", "grades": [18, 16, 19]},
]

for x, student in enumerate(students, start=1):
    print(f"{x}-{student['name']}: {student['grades']}")

for student in students:
    average=(student["grades"][0]+student["grades"][1]+student["grades"][2])/3
    student["average"]=average

    if average>=10:
        print(f"{student['name']}: {student['average']:.2f}-> pass")
    else:
        print(f"{student['name']}: {student['average']:.2f}-> fail")

print(any(student["average"]>=18 for student in students))

print(all(student["average"]>=10 for student in students))

gradess=[]

for student in students:
    for grade in student["grades"]:
        gradess.append(grade)
        unique_grades=set(gradess)

print(unique_grades)

name_search=input("enter student name: ")

for student in students:
    if name_search == student["name"]:
        print(student)
        break
else:
    print("student not found!!")