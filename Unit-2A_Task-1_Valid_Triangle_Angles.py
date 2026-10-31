a = float(input("Enter first angle in degrees: "))
b = float(input("Enter second angle in degrees: "))
c = float(input("Enter third angle in degrees: "))
if a + b + c == 180 and a > 0 and b > 0 and c > 0:
    print(f"The triangle with angles {a}, {b}, and {c} is valid")
else:
    print(f"The triangle with angles {a}, {b}, and {c} is not valid")
