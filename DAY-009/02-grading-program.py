
scores={
    "ankush":70,
    "john":90,
    "angela":99,
    "chaitanya":79,
    "wicker":71,
    "allen":78,
    "justin":88,
    "dustin":91,
    "eleven":76
}

print("Student Grades >>")
student_grades={}
for key in scores:
    key.capitalize()
    if scores[key] >=91:
        student_grades[key]="Outstanding😎"
    elif scores[key] >=81:
        student_grades[key]="Exceeds Expectation😀"
    elif scores[key] >=71:
        student_grades[key]="Acceptable😃"
    elif scores[key]<=70:
        student_grades[key]="Fail🥲"
    else:
        print("Invalid Score")
    
    print(f"  {key.capitalize()} = {student_grades[key]}")


