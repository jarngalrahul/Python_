from bs4 import BeautifulSoup
from pprint import pprint
import requests


class SearchZillowProperties:
    URL = f'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'

    def __init__(self):
        self.soup = self.create_soup()
        self.properties = {}
        self.links = []
        self.prices = []
        self.address = []

    def create_soup(self):
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                          '(KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
        }
        content = requests.get(url=SearchZillowProperties.URL, headers=header)
        content.raise_for_status()
        web_page = content.text
        return BeautifulSoup(web_page, 'html.parser')

    def search_properties(self):
        property_cards = self.soup.find_all(
            name='div', class_='property-card-data')
        for property_card in property_cards:
            addr = property_card.contents[0].string
            link = property_card.contents[0]['href']
            if 'https://www.zillow.com/' not in link:
                link = 'https://www.zillow.com/'+link
            price = property_card.contents[2].string.split('+')[0]
            self.address.append(addr)
            self.prices.append(price)
            self.links.append(link)

    def make_property_data(self) -> dict:
        for num in range(len(self.address)):
            self.properties[num] = {
                'address': self.address[num],
                'rent_price': self.prices[num],
                'link_to_property': self.links[num]
            }
        return self.properties
