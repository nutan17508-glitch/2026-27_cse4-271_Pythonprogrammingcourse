n = int(input("Enter how many numbers: "))
sum = 0

for i in range(n):
    num = int(input("Enter a number: "))
    sum = sum + num

average = sum / n

print(f"Sum of {n} numbers is {sum}")
print(f"Average of {n} numbers (sum {sum}) is {average}")