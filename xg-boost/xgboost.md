XGBoost is an algorithm that builds many small decision trees one after another.

Tree 1 is built using the original dataset and makes predictions.
XGBoost compares the predictions with the actual values and calculates the error (residual/gradient) for every training sample.
Tree 2 is built using the same input features, but instead of trying to predict the original target, it tries to predict how much Tree 1 was wrong (the residual).
After Tree 2 is trained, its predictions are added to Tree 1's predictions to produce a better prediction.
XGBoost again calculates the remaining error.
Tree 3 is trained to predict this new remaining error.
This process continues until the remaining error becomes very small or the maximum number of trees is reached.
During prediction (inference), all the trained trees are used. The input passes through every tree, each tree gives its output, and all those outputs are added together to produce the final prediction.