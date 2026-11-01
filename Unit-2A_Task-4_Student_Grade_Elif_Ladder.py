marks = int(input("Enter your marks: "))

if marks >= 90:
    print(f"Marks={marks},Grade A")
elif marks >= 80:
    print(f"Marks={marks},Grade B")
elif marks >= 70:
    print(f"Marks={marks},Grade C")
else:
    print(f"Marks={marks},Grade D")

