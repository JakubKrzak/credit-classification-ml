from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import numpy as np

from myproject.config.imputer_columns import (
    numeric,
    onehotencoder,
    creditmix,
    payment,
    log
    
)



def preprocessing_pipeline():
    numeric_median_pipe = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler()),
    ])
    
    # log_pipe = Pipeline([
    #     ('log', FunctionTransformer(np.log1p, validate=False)),
    #     ('scaler', StandardScaler()),
    # ])
    
    cat_OneHoteEncoder_pipe = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False)),
    ])
    
    credit_mix_pipe = Pipeline ([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('ordinal', OrdinalEncoder(
            categories=[["Bad", "Standard", "Good"]],
            handle_unknown='use_encoded_value',
            unknown_value= -1,
        ))
    ])
    
    payment_pipe = Pipeline ([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('ordinal', OrdinalEncoder(
            categories=[["No", "Yes"]],
            handle_unknown="use_encoded_value",
            unknown_value=-1
        ))
    ])
    
    preprocess = ColumnTransformer(
        transformers=[
            ('numeric', numeric_median_pipe, numeric ),
            ('onehot', cat_OneHoteEncoder_pipe, onehotencoder),
            ('creditmix', credit_mix_pipe, creditmix),
            ('payment', payment_pipe, payment)
        ],
        remainder='drop',
        n_jobs=-1
    
    )
    return preprocess