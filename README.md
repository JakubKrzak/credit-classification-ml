Exploratory Data Analysis (EDA)

A concise, text-driven EDA notebook is available here:
➡️ Open EDA Notebook
➡️ [Click to open the EDA notebook](notebooks/EDA_credit_score_text_first_part.ipynb)
Key points:

Dataset contains 100k+ monthly customer records (panel structure).

Target variable Credit_Score has 3 classes: Good, Standard, Poor (moderately imbalanced).

Several important columns contain missing values, inconsistent numeric formatting, and outliers (e.g., negative ages, unrealistic debt or account counts).

Feature groups include: demographics, income, loan types, delinquencies, utilisation ratios, behavioural patterns.

Strong expected predictors:
Credit_Utilization_Ratio, Num_of_Delayed_Payment, Num_Credit_Inquiries, Outstanding_Debt, Total_EMI_per_month, Payment_Behaviour, Credit_Mix.

Correlation structure shows clusters typical for credit-risk modelling; suitable for tree-based, non-linear models.

EDA Conclusion (short):

Data quality requires preprocessing (type fixing, outlier handling, imputation).

Clear behavioural patterns align with real credit-risk signals.

Feature distributions and correlations justify using boosting and ensemble methods.
