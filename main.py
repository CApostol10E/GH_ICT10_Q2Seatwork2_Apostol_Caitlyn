first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")

# Step 2: Define subjects and units
subjects = ["Science", "Mathematics", "English", "History", "PE"]
units = (3, 3, 3, 2, 1)  # Tuple for the number of units per subject

# Step 3: Get Grades from the user
grades = []
for subject in subjects:
    grade = float(input(f"Enter your grade in {subject}: "))
    grades.append(grade)

# Step 4: Calculate General Weighted Average (GWA)
total_units = sum(units)
weighted_sum = sum(g * u for g, u in zip(grades, units))
gwa = round(weighted_sum / total_units, 2)

# Step 5: Display Results
print("\n===== Student Information =====")
print(f"Name: {first_name} {last_name}")

print("\n===== Summary of Grades =====")
for subj, grade in zip(subjects, grades):
    print(f"{subj}: {grade}")

print("\n===== General Weighted Average =====")
print(f"GWA: {gwa}")