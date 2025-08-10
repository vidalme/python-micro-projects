from bs4 import BeautifulSoup
import requests


url = 'https://quotes.toscrape.com/tag/life/'

def main():
    print("This is the main function of the scrapper module.")
    # Add your scraping logic here
    r = requests.get(url)
    
    soup = BeautifulSoup(r.text,'html')

    print(soup.h1)

if __name__ == "__main__":
    main()