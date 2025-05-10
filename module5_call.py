#Bowei Bian Module5_call.py
from module5_mod import NumberList

def main():
    data = NumberList()

    # Get N
    while True:
        try:
            N = int(input("Enter the number of elements (N): "))
            if N <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    # Input N numbers
    for i in range(1, N + 1):
        while True:
            try:
                num = int(input(f"Enter number {i}: "))
                data.insert_number(num)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    # Get X to search
    while True:
        try:
            X = int(input("Enter the number to search for (X): "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Output result
    result = data.search(X)
    print(result)

if __name__ == "__main__":
    main()