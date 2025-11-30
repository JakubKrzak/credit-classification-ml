c_drop = ["ID", "Customer_ID", "Name", "SSN", "Type_of_Loan"]

c_ToNumRemoveChars = [
    "Age",
    "Annual_Income",
    "Monthly_Inhand_Salary",
    "Num_Bank_Accounts",
    "Num_Credit_Card",
    "Interest_Rate",
    "Delay_from_due_date",
    "Num_of_Delayed_Payment",
    "Changed_Credit_Limit",
    "Num_Credit_Inquiries",
    "Outstanding_Debt",
    "Credit_Utilization_Ratio",
    "Total_EMI_per_month",
    "Amount_invested_monthly",
    "Monthly_Balance",
    "Num_of_Loan"
]

c_Remove28 = ['Age', 'Annual_Income', 'Num_of_Delayed_Payment', 'Outstanding_Debt']

c_age = ["Age"]

c_ValueCliperq99 = [
    "Annual_Income",
    "Monthly_Inhand_Salary",
    "Delay_from_due_date",
    "Num_of_Delayed_Payment",
    "Num_Credit_Inquiries",
    "Credit_Utilization_Ratio",
]

c_ValueClipperq90 = [
    "Num_Bank_Accounts",
    "Num_Credit_Card",
    "Interest_Rate",
    "Amount_invested_monthly",
]

c_EmiPerMonthTransformer = ["Total_EMI_per_month"]

c_MonthlyBalance = ["Monthly_Balance"]

c_CreditMix = ["Credit_Mix"]

c_CreditHistoryAge = ["Credit_History_Age"]

c_PaymentOfMinAmount = ["Payment_of_Min_Amount"]

c_Behavior = ["Payment_Behaviour"]

c_Occupation = ["Occupation"]
