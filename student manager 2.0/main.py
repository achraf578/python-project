from student_add import new_student
import json
import os

if os.path.exists('student list.json'):
    with open('student list.json', 'r') as file:
        students=json.load(file)
else:
    students = []

grades=[]

answer= input("Do you want to add a new student? ").lower()
if answer == "yes":
    name=input("Please enter the sutudent's name: ").title()
    for i in range(3):
        grade=float(input("Enter the student's grade: "))
        grades.append(grade)
    students.append(new_student(name=name, grades=grades))

    with open ('student list.json', 'w') as file:
        json.dump(students, file)
else:
    print("Ok!")

with open ('student list.json', 'r') as file:
    students=json.load(file)
    
for x, student in enumerate(students, start=1):
    print(f"{x}-{student['name']}: {student['grades']}")

min_average=float(input("Please enter the minimum average: "))

for student in students:
    average=(student["grades"][0]+student["grades"][1]+student["grades"][2])/3
    student["average"]=round(average, 2)

    if average>=min_average:
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

students.sort(key= lambda item: item['average'])

for student in students:
    print(f"{student['name']}: {student['average']:.2f}")

name_search=input("enter student name: ").title()

for student in students:
    if name_search == student["name"]:
        print(student)
        break
else:
    print("student not found!!")

