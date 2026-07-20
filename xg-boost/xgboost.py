class SimpleTree:
    def __init__(self):
        self.split = None
        self.left_value = None
        self.right_value = None

    def fit(self, X, y):

        best_error = float("inf")

        for split in sorted(set(X)):

            left = []
            right = []

            for x, target in zip(X, y):
                if x < split:
                    left.append(target)
                else:
                    right.append(target)

            if len(left) == 0 or len(right) == 0:
                continue

            left_mean = sum(left) / len(left)
            right_mean = sum(right) / len(right)

            error = 0

            for x, target in zip(X, y):

                prediction = left_mean if x < split else right_mean

                error += (target - prediction) ** 2

            if error < best_error:
                best_error = error
                self.split = split
                self.left_value = left_mean
                self.right_value = right_mean

    def predict(self, X):

        predictions = []

        for x in X:

            if x < self.split:
                predictions.append(self.left_value)
            else:
                predictions.append(self.right_value)

        return predictions


# -----------------------------
# Dataset
# -----------------------------

X = [20, 25, 30, 35]
y = [100, 125, 150, 175]

# -----------------------------
# Initial prediction
# -----------------------------

predictions = [0] * len(y)

learning_rate = 1.0

trees = []

num_trees = 6

print("=" * 50)
print("Training Starts")
print("=" * 50)

for tree_number in range(num_trees):

    # Step 1 : Calculate Residuals
    residuals = []

    for actual, pred in zip(y, predictions):
        residuals.append(actual - pred)

    print(f"\nTree {tree_number + 1}")
    print("-" * 40)

    print("Current Prediction :", predictions)
    print("Residuals          :", residuals)

    # Step 2 : Train Tree
    tree = SimpleTree()
    tree.fit(X, residuals)

    trees.append(tree)

    # Step 3 : Tree predicts corrections
    correction = tree.predict(X)

    print("Tree Correction    :", correction)

    # Step 4 : Add correction
    for i in range(len(predictions)):
        predictions[i] += learning_rate * correction[i]

    print("Updated Prediction :", predictions)

print("\n")
print("=" * 50)
print("Training Completed")
print("=" * 50)

print("\nFinal Prediction")
print(predictions)

print("\nActual Values")
print(y)

print("\n")


# --------------------------------------------------------
# Inference
# --------------------------------------------------------

def predict(sample):

    result = 0

    print("\nInference")
    print("=" * 40)

    for i, tree in enumerate(trees):

        value = tree.predict([sample])[0]

        print(f"Tree {i+1} contributes {value}")

        result += learning_rate * value

    print("-" * 40)
    print("Final Prediction =", result)

    return result


predict(28)