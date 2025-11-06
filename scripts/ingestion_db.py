import pandas as pd
import os 
from sqlalchemy import create_engine

engine = create_engine('sqlite:///sales.db')
os.listdir()

for file in os.listdir('dataset'):
    df = pd.read_csv('dataset/'+file, encoding="latin-1")

df.to_sql(df, con=engine, if_exists='replace', index=False)