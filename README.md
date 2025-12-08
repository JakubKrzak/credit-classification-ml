1. Project Overview 🚀

This project focuses on building a multi-class credit scoring model that predicts a customer's Credit_Score (Good, Standard, Poor) based on their financial behaviour, income, credit utilisation, payment history, and loan structure.

Technologies Used 🛠️

Python 3.12

Pandas, NumPy, Matplotlib

Scikit-Learn

XGBoost, Random Forest, Gradient Boosting

MLflow for experiment tracking

Custom preprocessing pipelines (feature cleaning, extraction, transformations)

The goal is to create a model that mirrors real-world credit-risk systems using explainable, robust machine-learning techniques.



2. Exploratory Data Analysis (EDA) 🔍

A full, text-driven EDA notebook is available here:
➡️ Open EDA Notebook

Key insights:

Dataset contains 100,000+ monthly customer records (panel data).

Target Credit_Score is moderately imbalanced — F1_macro is used as the main metric.

Several variables contain missing data or inconsistent formats (e.g., numeric values stored as text).

Strong predictive features include:
Credit_Utilization_Ratio, Num_of_Delayed_Payment,
Num_Credit_Inquiries, Outstanding_Debt,
Total_EMI_per_month, Payment_Behaviour, Credit_Mix.

Overall behaviour of features aligns with real credit-risk patterns.

EDA conclusion: preprocessing and feature engineering are essential, and the dataset strongly favours tree-based ensemble methods.



3. Model Evaluation 📊

Several machine-learning models were trained and compared using F1_macro and Accuracy.
Below is a summary of the best performers.

<h3>Model Performance Summary</h3>

<table>
  <tr>
    <th>Model</th>
    <th>F1_macro</th>
    <th>Accuracy</th>
  </tr>

  <tr>
    <td><b>⭐ XGBoost (tuned)</b></td>
    <td><img src="https://img.shields.io/badge/0.782-brightgreen"></td>
    <td><img src="https://img.shields.io/badge/0.7939-brightgreen"></td>
  </tr>

  <tr>
    <td>🌲 Random Forest (tuned)</td>
    <td><img src="https://img.shields.io/badge/0.7806-green"></td>
    <td><img src="https://img.shields.io/badge/0.791-green"></td>
  </tr>

  <tr>
    <td>🌲 Random Forest (baseline)</td>
    <td><img src="https://img.shields.io/badge/0.770-yellowgreen"></td>
    <td><img src="https://img.shields.io/badge/0.785-yellowgreen"></td>
  </tr>

  <tr>
    <td>Gradient Boosting</td>
    <td><img src="https://img.shields.io/badge/0.678-yellow"></td>
    <td><img src="https://img.shields.io/badge/0.703-yellow"></td>
  </tr>

  <tr>
    <td>Decision Tree</td>
    <td><img src="https://img.shields.io/badge/0.685-orange"></td>
    <td><img src="https://img.shields.io/badge/0.708-orange"></td>
  </tr>

  <tr>
    <td>Logistic Regression</td>
    <td><img src="https://img.shields.io/badge/0.590-red"></td>
    <td><img src="https://img.shields.io/badge/0.620-red"></td>
  </tr>
</table>

