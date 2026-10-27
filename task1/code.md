# 1. University Scholarship Allocation System

## 1. Problem Statement
University Scholarship Allocation: Design a system that evaluates applicants using aggregate marks, subject-wise minimum scores, attendance, and income criteria, ranks eligible students, and resolves ties using predefined rules.

## 2. Algorithm

Step 1: Start the program.

Step 2: Read the number of students.

Step 3: For each student, accept:

- Student name
- Aggregate marks
- Subject-wise marks
- Attendance percentage
- Annual family income

Step 4: Check eligibility conditions:

- Aggregate marks ≥ 75
- Every subject mark ≥ 60
- Attendance ≥ 75
- Annual family income ≤ ₹2,50,000

Step 5: If all conditions are satisfied, add the student to the eligible list.

Step 6: Sort eligible students using the following priority:

1. Higher aggregate marks.
2. Higher attendance percentage.
3. Lower annual family income.

Step 7: Display the eligible students in ranked order.

Step 8: Display the ineligible students separately.

Step 9: Stop the program.

## 3. Flowchart
``` mermaid

flowchart TD
    A([Start]) --> B[/Enter number of students/]
    B --> C[/Enter student details/]
    C --> D[/Enter aggregate, subject marks, attendance and income/]

    D --> E{Aggregate >= 75?}

    E -- No --> I[Mark as Ineligible]
    E -- Yes --> F{All subject marks >= 60?}

    F -- No --> I
    F -- Yes --> G{Attendance >= 75?}

    G -- No --> I
    G -- Yes --> H{Income <= 250000?}

    H -- No --> I
    H -- Yes --> J[Add to Eligible List]

    I --> K{More students?}
    J --> K

    K -- Yes --> C
    K -- No --> L[Sort Eligible Students]

    L --> M[Rank by Aggregate Marks]
    M --> N[Break Ties by Attendance]
    N --> O[Break Remaining Ties by Lower Income]

    O --> P[/Display Scholarship Ranking/]
    P --> Q[/Display Ineligible Students/]
    Q --> R([Stop])


```




## 5. Sample Input

```
Enter number of students: 4

Enter details of Student 1
Enter student name: Arun
Enter aggregate marks: 85
Enter subject marks separated by spaces: 80 85 90
Enter attendance percentage: 90
Enter annual family income: 200000

Enter details of Student 2
Enter student name: Priya
Enter aggregate marks: 90
Enter subject marks separated by spaces: 90 92 88
Enter attendance percentage: 85
Enter annual family income: 220000

Enter details of Student 3
Enter student name: Rahul
Enter aggregate marks: 85
Enter subject marks separated by spaces: 75 80 85
Enter attendance percentage: 95
Enter annual family income: 180000

Enter details of Student 4
Enter student name: Sneha
Enter aggregate marks: 70
Enter subject marks separated by spaces: 65 70 75
Enter attendance percentage: 80
Enter annual family income: 150000
```

## 6. Sample Output

```
===== SCHOLARSHIP ELIGIBLE STUDENTS =====

Rank    Name      Aggregate   Attendance   Income

1       Priya     90.0        85.0         220000.0
2       Rahul     85.0        95.0         180000.0
3       Arun      85.0        90.0         200000.0

===== INELIGIBLE STUDENTS =====

Sneha
```

Explanation of Ranking:

- Priya gets Rank 1 because she has the highest aggregate marks (90%).
- Rahul gets Rank 2 because he has higher attendance (95%) than Arun.
- Arun gets Rank 3 because his attendance is 90%.
- Sneha is ineligible because her aggregate marks are below 75%.





