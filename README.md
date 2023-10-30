![pixar](https://github.com/niniet98/PROJECT-II/blob/main/images/pixar.jpg?raw=true)
# Pixar Scrapping & EDA

## Overview
The main goal of this project was to identify a dataset of particular interest and enhance it by retrieving additional information using web scraping techniques or APIs.

## Dataset & Data Source
- [Pixar Studio DataSet](https://www.kaggle.com/datasets/sandipdevre/pixar-studio12) from Kaggle.
- Web scrapping from [Pixar](https://www.pixar.com/).
- Web scrapping from [Pixar Films - Wikipedia](https://en.wikipedia.org/wiki/List_of_Pixar_films).


## Pipeline & Libraries

**1. Identification of the dataset of interest:**
This phase involved at first, the decision regarding the project subject followed by the search of a dataset or even exploring public data sources, online databases and creating a dataset from scratch if it was no available.

**2. Collection of additional data:**
Once the dataset identified, moved on to the phase of collecting additional relevant data. This was achieved using web scrapping techniques to extract information from relevant websites.

**3. Data cleaning and preparation:**
The collected data, both the original dataset and the additional data, underwent a process of cleaning and preparation. This included dropping columns with unupdated information, standarizing formats and creating new columns based on other columns information.

**4. Exploratory Data Analysis (EDA) and Visualizations:**
Once the data was clean and ready, an exploratory data analysis was conducted. This stage involved the application of statistical and visualization techniques to better understand the structure and relationships within the dataset as well as generating graphs in order to help communicate the results.

The code was written in Python and Jupyter Notebook. The following libraries have been used:
- Numpy
- Pandas
- matplotlib.pyplot
- Seaborn
- Requests
- BeautifulSoup

## Hypotheses
**1 & 2** - Concept art significantly influences film budgets by serving as a visual guide for the film's creative vision. The intricacy and quality of concept art impact resource allocation, potentially requiring investments in skilled artists and advanced software, which in turn can affect the overall budget of the production.

**3** - A fundamental financial imperative in the film industry is that revenue must surpass production budget expenditures. Moreover, the films that achieve the highest revenues attain a status of heightened popularity and commercial success within the industry.

## Storytelling

Regarding the extracted graph for this hypothesis, it is clear that the budget of a film varies depending on the conceptual work behind it as well as other important phases in the creation process, which in turn depends on the world you want to create. It is not the same to recreate the real world in a Pixar film such as 'Up', which recreates a city with its humans than to create the world of the new film 'Elemental' which has completely invented characters with visual effects, in addition to the different worlds that appear in the film.

![budget_art_design](https://github.com/niniet98/PROJECT-II/blob/main/figures/budget_art_design.png?raw=true)

Concerning about this graph, the budget increase may also be related to the advanced technologies that exist today to model the characters, animate them and render the final product with the highest possible quality. It may also be due to the rendering engine used by Pixar Studio.

![budget_over_years](https://github.com/niniet98/PROJECT-II/blob/main/figures/budget_over_years.png?raw=true)

Regarding the next graph, it's evident that the revenues have to be higher than the budget and also that the revenue is directly related with the popularity of the film which relies on box office earnings.

![budget_vs_revenue](https://github.com/niniet98/PROJECT-II/blob/main/figures/budget_vs_revenue.png?raw=true)

## Conclusions

The 3D animation industry has been revolutionized by rapid technological progress, leading to considerable budget expansions for films. Advanced tools, software, and rendering techniques have elevated animation quality, creating immersive, lifelike experiences. These technological advancements have unleashed creativity, enabling captivating storytelling and the creation of realistic characters and worlds. As a result, 3D animated films have become immensely popular among audiences of all ages.

Increased budgets allow studios to tap into top talent and invest in research and development, maximizing each film's potential. The financial success of high-budget projects, often measured by box office earnings, showcases the audience's willingness to invest in exceptional visual storytelling. This success reaffirms the value of technological innovation in the 3D animation industry.

## Links
[Support Canva](https://www.canva.com/design/DAFyvLtRtAg/2v18yy9IUpOimw4lw6XqHw/edit?utm_content=DAFyvLtRtAg&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)