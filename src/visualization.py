import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np

def budget_art_design(pixar_films: pd.DataFrame):
    sns.scatterplot(data=pixar_films, x='film', y='budget', hue='assets_+_characters', palette='Dark2', s=100)
    for i in range(pixar_films.shape[0]):
        plt.annotate(pixar_films["assets_+_characters"][i], (pixar_films["film"][i], pixar_films["budget"][i]), textcoords="offset points", xytext=(1, 1), fontsize=12, color='black')
    plt.xlabel('')
    plt.ylabel('Budget')
    plt.title('Relationship between Budget and amount of Characters & Assets')
    plt.legend(labels=[])
    plt.xticks(rotation=90)
    plt.savefig('figures/budget_art_design.png', bbox_inches='tight')

def budget_over_years(pixar_films: pd.DataFrame):
    sns.lmplot(data=pixar_films, x='year', y='budget', aspect=2, height=6, line_kws={'color': 'darkblue'}, scatter_kws={'color': 'darkblue'})
    plt.xlabel('Year')
    plt.ylabel('Budget')
    plt.title('Evolution of Movie Budgets Over the Years')
    plt.savefig('figures/budget_over_years.png', bbox_inches='tight')

def budget_vs_revenue(pixar_films: pd.DataFrame):
    pixar_subset = pixar_films.sort_values(by="worldwide", ascending=True)
    fig, ax = plt.subplots()
    bar_width = 0.4
    bar_positions = np.arange(len(pixar_subset))
    ax.barh(bar_positions, pixar_subset['budget'], bar_width, color='gold', label='Budget')
    ax.barh(bar_positions + bar_width, pixar_subset['worldwide'], bar_width, color='mediumpurple', label='Worldwide Revenues')
    ax.set_yticks(bar_positions + bar_width / 2)
    ax.set_yticklabels(pixar_subset['film'])
    ax.set_xlabel('Amount (in millions)')
    ax.set_title('Comparison of Budget vs. Worldwide Revenues per Film')
    ax.legend()
    fig.set_size_inches(16, 8)
    fig.savefig('figures/budget_vs_revenue.png')

def visualize():
    df = pd.read_csv("data/joined.csv")
    budget_art_design(df)
    budget_over_years(df)
    budget_vs_revenue(df)


    