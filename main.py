first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")

subjects = ["Science", "Mathematics", "English", "History", "PE"]
units = (3, 3, 3, 2, 1)  # Tuple for the number of units per subject

grades = []
for subject in subjects:
    grade = float(input(f"Enter your grade in {subject}: "))
    grades.append(grade)

total_units = sum(units)
weighted_sum = sum(g * u for g, u in zip(grades, units))
gwa = round(weighted_sum / total_units, 2)

print("\n===== Student Information =====")
print(f"Name: {first_name} {last_name}")

print("\n===== Summary of Grades =====")
for subj, grade in zip(subjects, grades):
    print(f"{subj}: {grade}")

def pos_or_neg(e):
    document.getElementById('output1').innerHTML = ''
    num1 = document.getElementById('num1').value


    if num1 > 0:
        display(f'Number {num1} is positive', target='output1')
    else:
        display(f'Number {num1} is negative', target='output1')

print("\n===== General Weighted Average =====")

print(f"GWA: {gwa}")
