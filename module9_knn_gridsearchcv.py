#Bowei Bian module9_knn_gridsearchcv.py
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def get_input_pairs(count, dataset_name=""):
    x_vals = []
    y_vals = []
    print(f"Enter {count} (x, y) pairs for {dataset_name} dataset:")
    for i in range(count):
        x = float(input(f"Enter x value for pair {i+1}: "))
        y = int(input(f"Enter y value for pair {i+1}: "))
        x_vals.append(x)
        y_vals.append(y)
    return np.array(x_vals).reshape(-1, 1), np.array(y_vals)

def main():
    # Read training data
    N = int(input("Enter number of training samples (N): "))
    X_train, y_train = get_input_pairs(N, "training")

    # Read test data
    M = int(input("Enter number of test samples (M): "))
    X_test, y_test = get_input_pairs(M, "test")

    best_k = 1
    best_accuracy = 0.0

    # Try k from 1 to 10
    for k in range(1, 11):
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        print(f"Accuracy for k={k}: {acc:.2f}")
        if acc > best_accuracy:
            best_accuracy = acc
            best_k = k

    print(f"\nBest k: {best_k}")
    print(f"Test Accuracy with best k: {best_accuracy:.2f}")

if __name__ == "__main__":
    main()