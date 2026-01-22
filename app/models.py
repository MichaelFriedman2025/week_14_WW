from pandas import DataFrame
import pandas as pd
from fastapi import UploadFile
import io


def read_csv_file(file:UploadFile):
    df = pd.read_csv(io.BytesIO(file.file.read()))
    return df 

def add_one_colomn(df:DataFrame):
    df["risk_level"] = pd.cut(df["range_km"],bins=[0,20,100,300,float("inf")],labels=["low","medium","high","extreme"],right=True)
    df["risk_level"] = df["risk_level"].astype(str)
    return df

def replace_null(df:DataFrame):
    df["manufacturer"] = df["manufacturer"].fillna("Unknown")
    return df

def doing_all(file:UploadFile):
    df = read_csv_file(file)
    df_wite_more_one_colomn = add_one_colomn(df)
    df = replace_null(df_wite_more_one_colomn)
    return df