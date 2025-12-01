from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import loguniform


config = {
    "cv_folds": 5,
    "random_state": 42,
    
    #zestaw metryk
    "scoring": {
        "accuracy": "accuracy",
        "balanced_accuracy": "balanced_accuracy",
        "f1_macro": "f1_macro",
        "precision_macro": "precision_macro",
        "recall_macro": "recall_macro",
    },
    
    #================hiperparametry===================
    "params": {
        
        #Logistic Regression hyperparameters
        "log_reg": {
            "clf__C": loguniform(1e-3, 1e3),
            "clf__penalty": ["l2"],
            "clf__solver": ["lbfgs"],
            "clf__class_weight": [None, "balanced"],
            "clf__multi_class": ["multinomial"],
            "clf__max_iter": [300,500,1000],
        },
        
        #Decision Tree hyperparamerters
        "d_tree": {
            "clf__max_depth": [3, 5, 7, 9, 12, None],
            "clf__min_samples_split": [2, 20, 50, 100, 200],
            "clf__min_samples_leaf": [1, 5, 10, 20, 50],
            "clf__criterion": ["gini", "entropy"],
            "clf__class_weight": [None, "balanced"],
            "clf__max_features": [None, "sqrt", "log2", 0.5],
            "clf__max_leaf_nodes": [None, 50, 100, 200, 500]
        },
        
        #Random Forest hyperparameters
        "random_forest": {
                "clf__n_estimators": [200, 300, 400, 500],
                "clf__max_depth": [10, 15, 20, 25, None],
                "clf__min_samples_leaf": [1, 2, 3, 5, 10],
                "clf__min_samples_split": [2, 5, 10, 15],
                "clf__max_features": ["sqrt", "log2", 0.5],
                "clf__bootstrap": [True],
                "clf__class_weight": [None, "balanced"],
        }
        
    }
}

#For making life easier :)
