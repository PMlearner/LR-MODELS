import numpy as np

class DecisionTreeRegressorScratch:
    def __init__(self, max_depth=5, min_samples_split=2):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.tree = None

    def fit(self, X, y):
        data = np.concatenate([X, y.reshape(-1, 1)], axis=1)
        self.tree = self._build_tree(data, depth=0)

    def predict(self, X):
        return np.array([self._predict_sample(x, self.tree) for x in X])

    # ===================
    # Tree building
    # ===================
    def _build_tree(self, data, depth):
        X, y = data[:, :-1], data[:, -1]

        # stopping conditions
        if (depth >= self.max_depth) or (len(y) < self.min_samples_split) or len(set(y)) == 1:
            return {"leaf": True, "value": np.mean(y)}

        # find best split
        feature_idx, threshold, mse = self._best_split(X, y)
        if feature_idx is None:
            return {"leaf": True, "value": np.mean(y)}

        # split data
        left_idx = X[:, feature_idx] <= threshold
        right_idx = X[:, feature_idx] > threshold

        left_subtree = self._build_tree(data[left_idx], depth + 1)
        right_subtree = self._build_tree(data[right_idx], depth + 1)

        return {
            "leaf": False,
            "feature": feature_idx,
            "threshold": threshold,
            "left": left_subtree,
            "right": right_subtree,
        }

    # ===================
    # Best split search
    # ===================
    def _best_split(self, X, y):
        best_feature, best_threshold = None, None
        best_mse = float("inf")
        n_samples, n_features = X.shape

        for feature in range(n_features):
            thresholds = np.unique(X[:, feature])
            for t in thresholds:
                left_y = y[X[:, feature] <= t]
                right_y = y[X[:, feature] > t]

                if len(left_y) == 0 or len(right_y) == 0:
                    continue

                mse_split = self._weighted_mse(left_y, right_y)
                if mse_split < best_mse:
                    best_mse = mse_split
                    best_feature = feature
                    best_threshold = t

        return best_feature, best_threshold, best_mse

    def _weighted_mse(self, left_y, right_y):
        n = len(left_y) + len(right_y)
        mse_left = np.var(left_y) * len(left_y)
        mse_right = np.var(right_y) * len(right_y)
        return (mse_left + mse_right) / n

    # ===================
    # Prediction
    # ===================
    def _predict_sample(self, x, tree):
        if tree["leaf"]:
            return tree["value"]

        feature, threshold = tree["feature"], tree["threshold"]
        if x[feature] <= threshold:
            return self._predict_sample(x, tree["left"])
        else:
            return self._predict_sample(x, tree["right"])
# Sample regression dataset
X = np.array([[1], [2], [3], [4], [5], [6], [7]])
y = np.array([1.1, 1.9, 3.0, 3.9, 5.1, 6.2, 7.1])

# Train tree
tree = DecisionTreeRegressorScratch(max_depth=3)
tree.fit(X, y)

# Predict
preds = tree.predict(np.array([[2.5], [5.5], [6.8]]))
print(preds)
