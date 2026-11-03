# This program prints the multiplication table of a given number using for loop.

n = int(input("Enter a number: ")) 

for i in range(1, 11):
    print(n, "x", i, "=", n * i)

# This program prints the multiplication table of a given number using while loop.

N = int(input("Enter a number: "))
i = 1

while i <= 10:
    print(N, "x", i, "=", N * i)
    i = i + 1
