from src import scrapping, cleaning, transforming, visualization

if __name__ == '__main__':
    scrapping.pixar_scrapping()
    scrapping.wikipedia_scrapping()
    cleaning.clean()
    transforming.transform()
    visualization.visualize()
