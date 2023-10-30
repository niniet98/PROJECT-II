import pandas as pd
from src import functions


def count_items(str_):
    list_ = str_.split(',')
    return len(list_)

def transform():
    # Original DataSet
    original_df = pd.read_csv('data/pixar__studio12.csv')
    original_df.rename(columns={'Moviename': 'film'}, inplace=True)
    original_df.rename(columns={'Releaseyear': 'year'}, inplace=True)
    original_df.rename(columns={'Rotten Tomatoes': 'rotten_tomatoes_score'}, inplace=True)
    original_df = original_df.drop(columns=['Budget(million)', 'US and canada(million)', 'Other territories(million)', 'Worldwide(million)', 'year'])
    # Characters & Assets DataSet
    char_assets_df = pd.read_csv('data/characters_assets.csv')
    # Acadey Awards DataSet
    academy_awards_df = pd.read_csv('data/pixar_academy_awards.csv')

    # Merging DataFrames
    final_df = pd.merge(original_df, char_assets_df, on="film", how="outer")
    final_df = pd.merge(final_df, academy_awards_df, on="film", how="outer")

    # Adding columns
    final_df['num_characters'] = final_df['characters'].apply(count_items)
    final_df['num_assets'] = final_df['assets'].apply(count_items)
    final_df['assets_+_characters'] = final_df['num_characters'] + final_df['num_assets']
    functions.export_to_csv(final_df, 'data/joined')

