#Bowei Bian module8_metrics-scikit.py
import numpy as np
from sklearn.metrics import precision_score, recall_score

def get_binary_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value in (0, 1):
                return value
            else:
                print("Please enter 0 or 1 only.")
        except ValueError:
            print("Invalid input. Please enter 0 or 1.")

def main():
    while True:
        try:
            N = int(input("Enter the number of data points (positive integer): "))
            if N > 0:
                break
            else:
                print("Number must be positive.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    # Initialize arrays to store true and predicted labels
    true_labels = np.zeros(N, dtype=int)
    predicted_labels = np.zeros(N, dtype=int)

    # Read in N (x, y) pairs
    for i in range(N):
        print(f"\nPoint {i + 1}:")
        x = get_binary_input("  Enter true label (x, 0 or 1): ")
        y = get_binary_input("  Enter predicted label (y, 0 or 1): ")
        true_labels[i] = x
        predicted_labels[i] = y

    # Calculate precision and recall
    precision = precision_score(true_labels, predicted_labels, zero_division=0)
    recall = recall_score(true_labels, predicted_labels, zero_division=0)

    # Output results
    print("\nResults:")
    print(f"  Precision: {precision:.2f}")
    print(f"  Recall:    {recall:.2f}")

if __name__ == "__main__":
    main()