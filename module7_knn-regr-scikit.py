#Bowei Bian module7_knn-regr-scikit.py
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.exceptions import NotFittedError

def main():
    # Read number of data points
    try:
        N = int(input("Enter the number of data points (N): "))
        if N <= 0:
            raise ValueError("N must be a positive integer.")
    except ValueError as ve:
        print(f"Invalid input for N: {ve}")
        return

    # Read the value of k
    try:
        k = int(input("Enter the number of neighbors (k): "))
        if k <= 0:
            raise ValueError("k must be a positive integer.")
    except ValueError as ve:
        print(f"Invalid input for k: {ve}")
        return

    # Validate k <= N
    if k > N:
        print("Error: k must be less than or equal to N.")
        return

    # Initialize data arrays
    X_data = np.zeros((N, 1), dtype=float)
    y_data = np.zeros(N, dtype=float)

    print("\nEnter your data points:")
    for i in range(N):
        try:
            x = float(input(f"Point {i+1} - Enter x: "))
            y = float(input(f"Point {i+1} - Enter y: "))
            X_data[i] = x
            y_data[i] = y
        except ValueError:
            print("Invalid input. x and y should be real numbers.")
            return

    # Output variance of the labels
    variance = np.var(y_data)
    print(f"\nVariance of Y values (labels): {variance:.4f}")

    # Ask for prediction input X
    try:
        X_input = float(input("\nEnter a value of X to predict Y: "))
    except ValueError:
        print("Invalid input. X should be a real number.")
        return

    # Fit the KNN regressor
    try:
        knn = KNeighborsRegressor(n_neighbors=k)
        knn.fit(X_data, y_data)
        y_pred = knn.predict(np.array([[X_input]]))
        print(f"Predicted Y value for X={X_input}: {y_pred[0]:.4f}")
    except Exception as e:
        print(f"An error occurred during prediction: {e}")

if __name__ == "__main__":
    main()