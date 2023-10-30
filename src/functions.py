import pandas as pd
import re
import requests
from bs4 import BeautifulSoup


# CLEANING
def rename_columns(df: pd.DataFrame):
    df.columns = [i.lower().replace(' ', '_') for i in df.columns]
    return df

def drop_null_rows(df: pd.DataFrame):
    df.dropna(how='all', inplace=True)
    return df

def drop_null_row_exclude_col(df: pd.DataFrame, col_arr: []):
    df = df[~df.drop(col_arr, axis=1).isna().all(axis=1)]
    return df

def drop_columns(df: pd.DataFrame, col_arr: []):
    df = df.drop(columns=col_arr)
    return df

# REGEX
def replace_pattern_by_string(df: pd.DataFrame, col: str, pattern, string: str):
    df.loc[:, col] = df[col].str.replace(pattern, string, regex=True)
    return df

# EXPORT
def export_to_csv(df: pd.DataFrame, path: str):
    df.to_csv(f'{path}.csv', index=False)

# HTML PARSER
def get_html(url):
    '''
    Returns de html parsed.
    '''
    res = requests.get(url)
    return BeautifulSoup(res.content, 'html.parser')
