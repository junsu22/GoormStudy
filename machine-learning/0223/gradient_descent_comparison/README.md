# Gradient Descent Optimization Comparison (Batch vs SGD vs Mini-Batch)

## 📌 Project Overview

This project explores and compares three Gradient Descent optimization
methods:

-   Batch Gradient Descent
-   Stochastic Gradient Descent (SGD)
-   Mini-Batch Gradient Descent

The goal is to understand how different update strategies affect
convergence speed and training stability using a real-world Kaggle
dataset.

------------------------------------------------------------------------

## 📊 Dataset

-   **Dataset:** House Prices --- Advanced Regression Techniques
    (Kaggle)
-   **Source:**
    https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques
-   **Samples:** 1460 houses
-   **Features:** 81 columns (including target `SalePrice`)
-   **Task:** Regression (House Price Prediction)

------------------------------------------------------------------------

## ⚙️ Data Preprocessing

-   Missing value handling
-   Categorical encoding using `pd.get_dummies()`
-   Feature scaling using `StandardScaler`
-   Train/Validation split

------------------------------------------------------------------------

## 🧠 Implemented Algorithms

### ✔ Batch Gradient Descent

-   Uses entire dataset per update
-   Stable convergence
-   Slower learning speed

### ✔ Stochastic Gradient Descent (SGD)

-   Updates weights for each individual sample
-   Fast learning start
-   High variance and instability with large learning rates

### ✔ Mini‑Batch Gradient Descent

-   Updates using small batches of data
-   Combines stability of Batch GD and speed of SGD
-   Widely used in modern deep learning

------------------------------------------------------------------------

## 📈 Results

Loss curves were compared across all three optimization methods.

Observations: - Batch GD converges smoothly but slowly. - SGD converges
quickly but shows oscillations. - Mini‑Batch GD achieves both fast
convergence and stable learning behavior.

Important Insight: Even with the same epoch count, learning differs
because update frequency varies. Fair comparison should consider
**update steps**, not only epochs.

------------------------------------------------------------------------

## 🧩 Key Takeaway

Mini‑Batch Gradient Descent provides the best balance between
computational efficiency and convergence stability, which is why it is
the standard optimization strategy in deep learning frameworks.

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   Python
-   NumPy
-   Pandas
-   Scikit‑learn
-   Matplotlib

------------------------------------------------------------------------

## 🚀 How to Run

1.  Download the dataset from Kaggle.
2.  Place `train.csv` in the project directory.
3.  Run the notebook or script to reproduce experiments and graphs.

------------------------------------------------------------------------

## ✨ Author

Machine Learning study project focusing on optimization fundamentals.
