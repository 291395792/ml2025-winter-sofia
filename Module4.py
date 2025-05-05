#Editor: Bowei Bian
N = int(input("Enter a positive integer N: ")) # Ask the user for the value of N

numbers = [] # Initialize an empty list to store the numbers

# Read N numbers from the user
for i in range(N):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

X = int(input("Enter an integer X: ")) # Ask the user for the value of X

# Check if X is in the list and output the result
if X in numbers:
    print(numbers.index(X) + 1)
else:
    print("-1")