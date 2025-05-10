#Bowei Bian Module5_oop.py
class NumberList:
    def __init__(self):
        self.numbers = []

    def insert_number(self, number):
        self.numbers.append(number)

    def search(self, x):
        try:
            # Return 1-based index
            return self.numbers.index(x) + 1
        except ValueError:
            return -1

def main():
    
    data = NumberList()# Initialize the NumberList object

    # Read the number of elements N
    while True:
        try:
            N = int(input("Enter the number of elements (N): "))
            if N <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    # Read N numbers
    for i in range(1, N + 1):
        while True:
            try:
                num = int(input(f"Enter number {i}: "))
                data.insert_number(num)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    # Read the value to search for
    while True:
        try:
            X = int(input("Enter the number to search for (X): "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Search and output result
    result = data.search(X)
    print(result)

if __name__ == "__main__":
    main()