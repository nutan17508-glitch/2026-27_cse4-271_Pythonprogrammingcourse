num = int(input("Enter a number between 1 and 100: "))
if num < 1 or num > 100:
    print(f"{num} is not between 1 and 100")
elif num == 1:
    print(f"{num} is not a prime number")
elif num in [2, 3, 5, 7]:
    print(f"{num} is a prime number")
elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
    print(f"{num} is not a prime number")
else:
    print(f"{num} is a prime number")
 