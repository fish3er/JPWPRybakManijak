import requests
from bs4 import BeautifulSoup
import json

def get_ceneo_data_from_json():
    url = 'https://www.ceneo.pl/Ekspresy_do_kawy'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')
    script_tag = soup.find('script', type='application/ld+json')

    if not script_tag:
        print("Nie znaleziono JSONa w <script>")
        return

    data = json.loads(script_tag.string)

    for item in data.get('itemListElement', []):
        product = item.get('item', {})
        name = product.get('name')
        price = product.get('offers', {}).get('lowPrice')
        if name and price:
            print(f"{name} - {price:.2f} zł")

if __name__ == "__main__":
    print("Ceneo - ekspresy do kawy:")
    get_ceneo_data_from_json()
