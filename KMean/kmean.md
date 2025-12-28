📌 K-Means Clustering — Simple & Interview-Ready Explanation

K-Means is an unsupervised machine learning algorithm used to group data into K clusters based on similarity.

👉 It groups data points such that:

Points in the same cluster are close to each other

Points in different clusters are far apart

🔹 How K-Means Works (Step-by-Step)

Choose K (number of clusters)

Initialize K centroids (randomly)

Assign each data point to the nearest centroid (using distance, usually Euclidean)

Recalculate centroids as the mean of assigned points

Repeat steps 3–4 until:

Centroids do not change OR

Max iterations reached

--------------------------------------------------------------------------------------------------------

🔹 Choosing the Right K
🔸 Elbow Method

Plot K vs WCSS (Within-Cluster Sum of Squares)

Choose the point where the curve bends (elbow)

🔸 Silhouette Score

Measures how well points fit within their cluster