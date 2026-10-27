
# University Scholarship Allocation System

students = []
eligible_students = []
ineligible_students = []

# Scholarship eligibility criteria
MIN_AGGREGATE = 75
MIN_SUBJECT_MARK = 60
MIN_ATTENDANCE = 75
MAX_INCOME = 250000

n = int(input("Enter number of students: "))

# Input student details
for i in range(n):
    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")
    aggregate = float(input("Enter aggregate marks: "))

    subjects = list(map(float, input(
        "Enter subject marks separated by spaces: "
    ).split()))

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    # Check eligibility
    if (aggregate >= MIN_AGGREGATE
        and all(mark >= MIN_SUBJECT_MARK for mark in subjects)
        and attendance >= MIN_ATTENDANCE
        and income <= MAX_INCOME):

        eligible_students.append({
            "name": name,
            "aggregate": aggregate,
            "attendance": attendance,
            "income": income
        })

    else:
        ineligible_students.append(name)

# Ranking based on predefined tie-breaking rules
eligible_students.sort(
    key=lambda x: (
        -x["aggregate"],
        -x["attendance"],
        x["income"]
    )
)

# Display eligible students
print("\n===== SCHOLARSHIP ELIGIBLE STUDENTS =====")

if eligible_students:
    print("\nRank\tName\t\tAggregate\tAttendance\tIncome")

    for rank, student in enumerate(eligible_students, 1):
        print(
            rank, "\t",
            student["name"], "\t\t",
            student["aggregate"], "\t\t",
            student["attendance"], "\t\t",
            student["income"]
        )
else:
    print("No eligible students found.")

# Display ineligible students
print("\n===== INELIGIBLE STUDENTS =====")

if ineligible_students:
    for name in ineligible_students:
        print(name)
else:
    print("All students are eligible.")
