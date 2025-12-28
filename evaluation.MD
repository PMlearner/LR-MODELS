LLM Evaluation Metrics

    Perplexity

        Measures how well the probability distribution predicted by the model matches the actual data.

        Formula: it’s the exponential of the average negative log-likelihood of tokens.

        Lower perplexity = better language modeling ability (model is less "surprised" by the text).

        ⚠️ Limitation: Only works for generative language modeling tasks (not for open-ended QA or classification).

    BLEU / ROUGE

    BLEU (Bilingual Evaluation Understudy):

        Based on n-gram precision → checks how many n-grams from model output appear in reference text.

        Includes a brevity penalty to avoid very short answers scoring high.

        Common in machine translation, summarization.

    ROUGE (Recall-Oriented Understudy for Gisting Evaluation):

        Focuses on recall of n-grams → how much of the reference text is covered by the model output.

        Especially useful in summarization (checking coverage of reference content).

    Accuracy

        Measures proportion of exact matches between model predictions and ground truth.

        Works well for classification-style tasks (e.g., intent detection, sentiment analysis, yes/no answers).

ML Evaluvation:
        🔹 Classification

            Accuracy

            Precision

            Recall (Sensitivity)

            Specificity

            F1 Score

            ROC-AUC

            PR-AUC (Precision-Recall AUC)

            Log Loss (Cross-Entropy Loss)

            Confusion Matrix

        🔹 Regression

            Mean Absolute Error (MAE)

            Mean Squared Error (MSE)

            Root Mean Squared Error (RMSE)

            R² (Coefficient of Determination)

            Adjusted R²

            Mean Absolute Percentage Error (MAPE)

            Huber Loss

        🔹 Unsupervised (Clustering / Dimensionality Reduction)

            Silhouette Score

            Davies-Bouldin Index

            Dunn Index

            Rand Index (RI)

            Adjusted Rand Index (ARI)

            Mutual Information (MI)

            Normalized Mutual Information (NMI)

            Calinski-Harabasz Index

            Elbow Method

            Gap Statistic

            Explained Variance (for PCA/Dimensionality Reduction)