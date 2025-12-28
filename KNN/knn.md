KNN stores:

Feature values

Corresponding labels

Training ends here (no calculations).

🔹 Prediction Phase (Actual Work Happens Here)

When a new data point comes:

Compute distance between new point and all training points

Select K nearest neighbors

Predict using:

Majority vote (classification)

Mean value (regression)




standard scaler and min maxscaler:
“StandardScaler standardizes data using mean and standard deviation, while MinMaxScaler rescales data to a fixed range like 0 to 1.”