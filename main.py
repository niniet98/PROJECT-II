from src import scrapping, cleaning, transforming, visualizing

if __name__ == '__main__':
    scrapping.pixar_scrapping()
    scrapping.wikipedia_scrapping()
    cleaning.clean()
    transforming.transform()
    visualizing.visualize()
