import pandas as pd

def load_titanic_data(filepath: str) -> pd.DataFrame:
    try:
        df = pd.read_csv("C:/Users/Laptop Land/Desktop/data science assignment 3/week-3-introduction-to-tabular-data-part1-faisalziakhan/data/titanic.csv")
        return df
    except FileNotFoundError:
        print(f"Error: The file at {filepath} was not found.")
        return pd.DataFrame()  
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return pd.DataFrame()  
    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame()  

