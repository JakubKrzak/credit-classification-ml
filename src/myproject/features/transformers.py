import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


class Drop(BaseEstimator, TransformerMixin):
    def __init__(self, target_cols=None):
        self.target_cols = target_cols

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = pd.DataFrame(X).copy()
        
        X = X.drop(columns=self.target_cols, errors="ignore")

        return X
  
class Remove28(BaseEstimator, TransformerMixin):
    def __init__(self, remove='28_',target_cols=None):
        self.remove = remove
        self.target_cols = target_cols

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = pd.DataFrame(X).copy()
        
        for col in self.target_cols:
            X[col] = X[col].astype(str)
            X[col] = X[col].str.replace(self.remove, "", regex=False)

        return X

class ToNumRemoveChars(BaseEstimator, TransformerMixin):
    def __init__(self, chars_to_remove=r"[^0-9.,]+", target_cols=None):
        self.chars_to_remove = chars_to_remove
        self.target_cols = target_cols

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = pd.DataFrame(X).copy()


        for col in self.target_cols:
            X[col] = X[col].astype(str)
            X[col] = X[col].str.replace(self.chars_to_remove, "", regex=True)
            X[col] = X[col].str.replace(",", ".", regex=False)
            X[col] = pd.to_numeric(X[col], errors="coerce")

        return X


class AgeTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, target_cols=None):
        self.min_age = 18
        self.max_age = 100
        self.target_cols = target_cols

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = pd.DataFrame(X).copy()

        for col in self.target_cols:
            X[col] = pd.to_numeric(X[col], errors='coerce')
            
            mask = (X[col] < self.min_age) | (X[col] > self.max_age)
            X.loc[mask, col] = np.nan
        
        return X


class ValueCliperq99(BaseEstimator, TransformerMixin):
    def __init__(self, q_max=0.99, target_cols=None):
        self.q_max = q_max
        self.target_cols = target_cols
        self.borders_ = {}

    def fit(self, X, y=None):
        X = pd.DataFrame(X).copy()
        self.borders_ = {}
        
        for col in self.target_cols:
           X[col] = pd.to_numeric(X[col], errors='coerce')
           self.borders_[col] = X[col].quantile(self.q_max)

        return self

    def transform(self, X):
        X = pd.DataFrame(X).copy()

        for col in self.target_cols:
            X[col] = pd.to_numeric(X[col], errors="coerce")
            X[col] = X[col].clip(upper=self.borders_[col])

        return X


class ValueClipperq90(BaseEstimator, TransformerMixin):
    def __init__(self, q_max=0.90, target_cols=None):
        self.q_max = q_max
        self.target_cols = target_cols
        self.borders_ = {}

    def fit(self, X, y=None):
        X = pd.DataFrame(X).copy()
        
        self.borders_ = {}
        
        for col in self.target_cols:
            X[col] = pd.to_numeric(X[col], errors='coerce')
            self.borders_[col] = X[col].quantile(self.q_max)
            
        return self
        
    def transform(self, X):
        X = pd.DataFrame(X).copy()

        for col in self.target_cols:
            X[col] = pd.to_numeric(X[col], errors='coerce')
            X[col] = X[col].clip(upper=self.borders_[col])

        return X


class EmiPerMonthTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, q_max=0.94, target_cols=None):
        self.q_max = q_max
        self.target_cols = target_cols
        self.borders_ = {}

    def fit(self, X, y=None):
        X = pd.DataFrame(X).copy()
        
        self.borders_ = {}

        for col in self.target_cols:
            X[col] = pd.to_numeric(X[col], errors='coerce')
            self.borders_[col] = X[col].quantile(self.q_max)

        return self

    def transform(self, X):
        X = pd.DataFrame(X).copy()

        for col in self.target_cols:
            X[col] = pd.to_numeric(X[col], errors='coerce')
            low = X[col] < 0
            high = X[col] > self.borders_[col]
            X.loc[low | high, col] =np.nan

        return X


class MonthlyBalance(BaseEstimator, TransformerMixin):
    def __init__(self, target_cols=None):
        self.target_cols = target_cols

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = pd.DataFrame(X).copy()

        for col in self.target_cols:
            X[col] = pd.to_numeric(X[col], errors="coerce")
            X.loc[(X[col] <= 0), col] = np.nan

        return X





class CreditMix(BaseEstimator, TransformerMixin):
    def __init__(self, placeholder="_", target_cols=None):
        self.placeholder = placeholder
        self.target_cols = target_cols

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = pd.DataFrame(X).copy()

        for col in self.target_cols:
            X[col] = X[col].astype(str)
            X[col] = X[col].str.replace(self.placeholder, "", regex=False)
        return X
        


class CreditHistoryAge(BaseEstimator, TransformerMixin):
    def __init__(self, extract_data=r"(\d+)\s*Years?(?:.*?(\d+)\s*Months?)?", target_cols=None):
        self.extract_data = extract_data
        self.target_cols = target_cols

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = pd.DataFrame(X).copy()

        for col in self.target_cols:
            s = X[col].astype(str)
            parts = s.str.extract(self.extract_data, expand=True)
            parts = parts.fillna(0)
            parts = parts.astype(float)
            

            months = parts.iloc[:, 0] * 12 + parts.iloc[:, 1]
            months = months.mask(months <= 0)
            years = months / 12
            X[col] = years
        
        return X


class PaymentOfMinAmount(BaseEstimator, TransformerMixin):
    def __init__(self, placeholder="NM", target_cols=None):
        self.placeholder = placeholder
        self.target_cols = target_cols

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = pd.DataFrame(X).copy()

        for col in self.target_cols:
            payment = X[col].astype(str)
            payment = payment.str.replace(self.placeholder, "", regex=False)
            X[col] = payment

       
        return X


class Behavior(BaseEstimator, TransformerMixin):
    def __init__(self, placeholder="!@9#%8", target_cols=None):
        self.placeholder = placeholder
        self.target_cols = target_cols

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = pd.DataFrame(X).copy()

        for col in self.target_cols:
            behavior = X[col].astype(str)
            behavior = behavior.str.replace(self.placeholder, "", regex=False)
            X[col] = behavior
        
        return X


class Occupation(BaseEstimator, TransformerMixin):
    def __init__(self, placeholder="_______", target_cols=None):
        self.placeholder = placeholder
        self.target_cols = target_cols

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = pd.DataFrame(X).copy()

        for col in self.target_cols:
            occupation = X[col].astype(str)
            occupation = occupation.str.replace(self.placeholder, "", regex=False)
            X[col] = occupation

        
        return X
