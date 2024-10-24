import pandas as pd

def get_numerical_df(df: pd.DataFrame, numerical_features: list) -> pd.DataFrame:
  
    numerical_df = df[numerical_features].copy()
   
    return numerical_df
    pass