#Bowei Bian module6_knn-regr.py
import numpy as np

def knn_regression(points, query_x, k):
    # Convert list to NumPy array for easier processing
    points_array = np.array(points)  # Shape: (N, 2)
    x_values = points_array[:, 0]
    y_values = points_array[:, 1]

    # Compute L2 distances from query_x to all x-values
    distances = np.abs(x_values - query_x)

    # Get the indices of the k nearest neighbors
    nearest_indices = np.argsort(distances)[:k]

    # Return the mean of the y-values of the k nearest neighbors
    return np.mean(y_values[nearest_indices])

def main():
    try:
        N = int(input("Enter the number of data points (N): "))
        k = int(input("Enter the number of neighbors (k): "))

        if N <= 0 or k <= 0:
            print("Error: N and k must be positive integers.")
            return

        if k > N:
            print("Error: k cannot be greater than N.")
            return

        points = []
        for i in range(N):
            x = float(input(f"Enter x value for point {i + 1}: "))
            y = float(input(f"Enter y value for point {i + 1}: "))
            points.append((x, y))

        query_x = float(input("Enter the query x value: "))
        prediction = knn_regression(points, query_x, k)
        print(f"Predicted y value using {k}-NN Regression: {prediction:.4f}")

    except ValueError:
        print("Invalid input. Please enter numeric values where required.")

if __name__ == "__main__":
    main()