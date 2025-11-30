from sklearn.pipeline import Pipeline

from myproject.features.transformers import (
    Drop,
    ToNumRemoveChars,
    AgeTransformer,
    ValueCliperq99,
    ValueClipperq90,
    EmiPerMonthTransformer,
    MonthlyBalance,
    CreditMix,
    CreditHistoryAge,
    PaymentOfMinAmount,
    Behavior,
    Occupation,
    Remove28,
)

from myproject.config.cleaning_columns import (
    c_drop,
    c_ToNumRemoveChars,
    c_age,
    c_ValueCliperq99,
    c_ValueClipperq90,
    c_EmiPerMonthTransformer,
    c_MonthlyBalance,
    c_CreditMix,
    c_CreditHistoryAge,
    c_PaymentOfMinAmount,
    c_Behavior,
    c_Occupation,
    c_Remove28
)


def cleaning_pipeline():
    clean_pipeline = Pipeline(
        [
            ("drop", Drop(target_cols=c_drop)),
            ("num_clean", ToNumRemoveChars(target_cols=c_ToNumRemoveChars)),
            ("age", AgeTransformer(target_cols=c_age)),
            ("clipp99", ValueCliperq99(target_cols=c_ValueCliperq99)),
            ("clipp90", ValueClipperq90(target_cols=c_ValueClipperq90)),
            ("emi", EmiPerMonthTransformer(target_cols=c_EmiPerMonthTransformer)),
            ("monthlyb", MonthlyBalance(target_cols=c_MonthlyBalance)),
            ("credit_mix", CreditMix(target_cols=c_CreditMix)),
            ("credit_age", CreditHistoryAge(target_cols=c_CreditHistoryAge)),
            ("payment_min", PaymentOfMinAmount(target_cols=c_PaymentOfMinAmount)),
            ("behavior", Behavior(target_cols=c_Behavior)),
            ("occupation", Occupation(target_cols=c_Occupation)),
            ('28', Remove28(target_cols=c_Remove28))
        ]
    )
    return clean_pipeline
