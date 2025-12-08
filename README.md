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

### Model Performance Summary

| Model | F1_macro | Accuracy |
|-------|---------|----------|
| ⭐ **XGBoost (tuned)** | ![f1](https://img.shields.io/badge/0.782-brightgreen) | ![acc](https://img.shields.io/badge/0.7939-brightgreen) |
| 🌲 Random Forest (tuned) | ![f1](https://img.shields.io/badge/0.7806-green) | ![acc](https://img.shields.io/badge/0.791-green) |
| 🌲 Random Forest (baseline) | ![f1](https://img.shields.io/badge/0.770-yellowgreen) | ![acc](https://img.shields.io/badge/0.785-yellowgreen) |
| Gradient Boosting | ![f1](https://img.shields.io/badge/0.678-yellow) | – |
| Decision Tree | ![f1](https://img.shields.io/badge/0.685-orange) | – |
| Logistic Regression | ![f1](https://img.shields.io/badge/0.590-red) | – |
