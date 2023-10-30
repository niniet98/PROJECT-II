import pandas as pd
import re
from src import functions

def clean_budget(str_):
    rgx = r'\d+'
    res = re.search(rgx, str_)
    if res:
        return int(res.group())
    return ''

def clean_money_cell(str_):
    regex_other = r'\$\d{1,3}(?:,\d{3})*(?:\.\d+)?'
    res = re.search(regex_other, str_)
    if res:
        res = res.group()
        res = res.replace(',', '').replace('$','')
        return round(int(res) / 1000000)
    return ''

def clean():
    # Import Academy Awards DataSet
    academy_awards_df = pd.read_csv('data/pixar_academy_awards.csv')
    academy_awards_df['budget'] = academy_awards_df['budget'].apply(clean_budget)
    academy_awards_df['u.s._and_canada'] = academy_awards_df['u.s._and_canada'].apply(clean_money_cell)
    academy_awards_df['other_territories'] = academy_awards_df['other_territories'].apply(clean_money_cell)
    academy_awards_df['worldwide'] = academy_awards_df['worldwide'].apply(clean_money_cell)
    functions.export_to_csv(academy_awards_df, 'data/pixar_academy_awards')

