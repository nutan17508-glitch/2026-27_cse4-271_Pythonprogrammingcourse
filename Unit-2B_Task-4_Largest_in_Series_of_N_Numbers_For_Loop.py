n=int(input("Enter how many numbers: "))
largest = float(input("Enter a number: ")) 

for _ in range(n - 1): 
    num = float(input("Enter a number: ")) 
    if num > largest: 
        largest = num 

print(f"Largest among {n} numbers is {largest}")
