from src import functions
import pandas as pd

def get_section_elements(m_html, num_sec):
    '''
    Returns a list of characters, assets (depends on the html number section).
    '''
    section = m_html.find_all('section')
    characters = section[num_sec].find_all('h2')
    return [i.getText() for i in characters]

def get_movies_dict(base_url, movies, num_sec):
    '''
    Returns a list of dictionaries.
    '''
    movies_dict_list = []
    for m in movies:
        name = m.getText()
        name = name.strip()
        link = m.find('a')
        link = link.get('href')
        request_url = f'{base_url}{link}'
        m_html = functions.get_html(request_url)
        characters = get_section_elements(m_html, num_sec)
        movies_dict_list.append({name: characters})
    return movies_dict_list

def get_pixar_movie_list(url):
    soup = functions.get_html(url)
    return soup.find_all('div', {'class':'slide'})

def clean_string_list(list_):
    str_ = ", ".join(list_)
    return str_.strip()

def build_df_structure(list_):
    movie_names = []
    list_of_lists = []
    for i in list_:
        for key, value in i.items():
            movie_names.append(key)
            list_of_lists.append(value)
    return [movie_names, list_of_lists]

def extract_wiki_table(rows, columns):
    # dictionary to control rowspan values in each iteration
    rowspan_values = {col: 1 for col in columns}
    data = []

    for idx, row in enumerate(rows):
        # list_ will be the list of values for each row in the table
        list_ = []
        cells = row.find_all('td')
        count_cells = 0
        for i in range(len(columns)):
            # check if last_row[column] rowspan is greater than 1 to pick the value of that cell
            # update rowspan of this row decreasing in 1
            if int(rowspan_values[columns[i]]) > 1:
                last_row = data[idx - 1]
                last_value = last_row[i]
                list_.append(last_value)
                rowspan_values[columns[i]] -= 1
            else:
                list_.append(cells[count_cells].getText().strip().replace('\\n', ''))
                if cells[count_cells].get('rowspan'):
                    rowspan_values[columns[i]] = int(cells[count_cells].get('rowspan'))
                else:
                    rowspan_values[columns[i]] = 1
                count_cells += 1
        data.append(list_)
    
    return pd.DataFrame(data, columns=columns)


# PIXAR
def pixar_scrapping():
    base_url = 'https://www.pixar.com'
    endpoint = '/feature-films-launch'
    request_url = f'{base_url}{endpoint}'
    soup = functions.get_html(request_url)
    movies = soup.find_all('div', {'class':'slide'})
    # Characters scrapping
    characters_section = 2
    movies = get_pixar_movie_list(request_url)
    characters_dict = get_movies_dict(base_url, movies, characters_section)
    # Assets scrapping
    assets_section = 4
    movies = get_pixar_movie_list(request_url)
    assets_dict = get_movies_dict(base_url, movies, assets_section)
    # Build DataFrames
    list_ = build_df_structure(characters_dict)
    df_structure = {
        'film': list_[0],
        'characters': list_[1]
    }
    characters_df = pd.DataFrame(df_structure)
    list_ = build_df_structure(assets_dict)
    df_structure = {
        'film': list_[0],
        'assets': list_[1]
    }
    assets_df = pd.DataFrame(df_structure)
    # Merge DataFrames
    merged_df = pd.merge(characters_df, assets_df, on='film', how='inner')
    # Clean merged DataFrames
    merged_df['characters'] = merged_df['characters'].apply(clean_string_list)
    merged_df['assets'] = merged_df['assets'].apply(clean_string_list)
    # Export
    merged_df.to_csv('data/characters_assets.csv', index=False)


# WIKIPEDIA
def wikipedia_scrapping():
    wiki = 'https://en.wikipedia.org/wiki/List_of_Pixar_films'
    soup = functions.get_html(wiki)
    wrappers = soup.find_all('table', {'class':'wikitable'})

    # Academy Award Table
    col_names = wrappers[4].find_all('th')
    col_names = [i.getText().strip() for i in col_names]
    col_names.remove('Sound[a]')
    col_names = [i.lower().replace(' ', '_') for i in col_names]
    col_names.remove('other')
    col_names.append('other')
    rows = wrappers[4].find_all('tr')
    rows = rows[2::]
    # Excluding 4 last rows to extract the info
    rows = rows[:22]
    df_1 = extract_wiki_table(rows, col_names)
    # The last 4 movies in the table from wikipedia were added by hand because there was a problem with the columns, which did not match.
    remaining_movies = [
    ['Soul', '', 'Won', '', 'Ineligible', 'Won', '', 'Nominated', 'Nominated', ''],
    ['Luca', '', 'Nominated', '', 'Ineligible', '', '', '', '', ''],
    ['Turning Red', '', 'Nominated', '', 'Ineligible', '', '', '', '', ''],
    ['Lightyear', '', '', 'Ineligible', '', '', '', '', '', '']
]
    df_2 = pd.DataFrame(remaining_movies, columns=col_names)
    # The two data frames were then concatenated to merge them into one.
    academy_awards_df = pd.concat([df_1, df_2], ignore_index=True)

    # Box Office Table
    col_names = wrappers[2].find_all('th')
    col_names = [i.getText().strip() for i in col_names]
    col_names.remove('Box office gross')
    col_names = [i.lower().replace(' ', '_') for i in col_names]
    col_names.remove('ref.')
    col_names.append('ref.')
    rows = wrappers[2].find_all('tr')
    rows = rows[2::]
    df = extract_wiki_table(rows, col_names)
    df = df.drop(columns=["ref."])

    # Merge and export
    final_df = pd.merge(academy_awards_df, df, on="film", how="outer")
    final_df.to_csv('data/pixar_academy_awards.csv', index=False)
