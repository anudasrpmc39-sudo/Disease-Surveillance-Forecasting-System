from sqlalchemy import create_engine
import pandas as pd
from config import DB_URL

engine = create_engine(DB_URL)

def save_data(df):
    df.to_sql("cases", engine, if_exists="replace", index=False)

def load_data():
    return pd.read_sql("SELECT * FROM cases", engine)
