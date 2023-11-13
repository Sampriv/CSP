# Paul kim was very help ful with the main part of the code

def add_assignment(grades_dict, category, grade):
    if category in grades_dict:
        grades_dict[category].append(float(grade))
    else:
        grades_dict[category] = [float(grade)]
    return grades_dict


grades_dict = {}

grades_dict = add_assignment(grades_dict, 'homework', 10)
grades_dict = add_assignment(grades_dict, 'homework', 50)
grades_dict = add_assignment(grades_dict, 'tests', 90)


def calculate_grade(grades_dict):
    homework_avg = sum(grades_dict['homework']) / len(grades_dict['homework'])
    test_avg = sum(grades_dict['tests']) / len(grades_dict['tests'])
    if 'labs' in grades_dict:
        lab_avg = sum(grades_dict['labs']) / len(grades_dict['labs'])
    else:
        lab_avg = 0
    grade_calculation = homework_avg * 0.2 + test_avg * 0.3 + lab_avg * 0.5
    return grade_calculation


print("Menu:")
print("1. Add Assignment")
print("2. Calculate Grade")
q1 = input("Enter your choice: ")

if q1 == 1:
    category = input("Enter category (homework tests labs): ").lower()
    grade = input("Enter grade for the assignment: ")
    grades_dict = add_assignment(grades_dict, category, grade)
    print(f"Assignment added to {category} category.")
elif q1 == 2:
    if grades_dict:
        final_grade = calculate_grade(grades_dict)
        print("Student's final grade:", final_grade)
    else:
        print("No assignments added yet. Cannot calculate grade.")
else:
    print("Invalid Input")
