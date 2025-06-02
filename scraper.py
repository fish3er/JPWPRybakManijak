import requests
from bs4 import BeautifulSoup

def get_mediaexpert_data():
    url = 'https://www.mediaexpert.pl/agd-male/ekspresy-i-kawa/ekspresy-cisnieniowe'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    products = soup.find_all('div', class_='offer-box')
    for product in products:
        name_tag = product.find('a', class_='name')
        price_tag = product.find('div', class_='price')
        if name_tag and price_tag:
            name = name_tag.get_text(strip=True)
            price = price_tag.get_text(strip=True)
            print(f"{name} - {price}")

def get_ceneo_data():
    url = 'https://www.ceneo.pl/Ekspresy_do_kawy'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    products = soup.find_all('div', class_='cat-prod-row')
    for product in products:
        name_tag = product.find('strong', class_='cat-prod-row__name')
        price_tag = product.find('span', class_='price')
        if name_tag and price_tag:
            name = name_tag.get_text(strip=True)
            price = price_tag.get_text(strip=True)
            print(f"{name} - {price}")

def get_allegro_data():
    url = 'https://allegro.pl/kategoria/do-kuchni-ekspresy-do-kawy-258232'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    products = soup.find_all('div', class_='opbox-listing--base')
    for product in products:
        name_tag = product.find('h2', class_='mgn2_14 mgn2_14_s')
        price_tag = product.find('span', class_='mgn2_14 mgn2_14_s')
        if name_tag and price_tag:
            name = name_tag.get_text(strip=True)
            price = price_tag.get_text(strip=True)
            print(f"{name} - {price}")

if __name__ == "__main__":
    print("MediaExpert:")
    get_mediaexpert_data()
    print("\nCeneo:")
    get_ceneo_data()
    print("\nAllegro:")
    get_allegro_data()
