# Bowei Bian Module5_mod.py
class NumberList:
    def __init__(self):
        self.numbers = []

    def insert_number(self, number):
        self.numbers.append(number)

    def search(self, x):
        try:
            return self.numbers.index(x) + 1  # Return 1-based index
        except ValueError:
            return -1