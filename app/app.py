import requests
from bs4 import BeautifulSoup
import json

class WebsiteIterator:
    def __init__(self, base_url, max_pages=1):
        self.base_url = base_url
        self.current_page = 1
        self.max_pages = max_pages
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_page > self.max_pages:
            raise StopIteration
        url = f"{self.base_url}?page={self.current_page}"
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            raise StopIteration
        self.current_page += 1
        # print("next page")
        return response.text


# def extract_product_data(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     script_tag = soup.find('script', type='application/ld+json')
#     if not script_tag:
#         return  # Brak danych
#
#     try:
#         data = json.loads(script_tag.string)
#         for item in data.get('itemListElement', []):
#             product = item.get('item', {})
#             name = product.get('name')
#             price = product.get('offers', {}).get('lowPrice')
#             rating = product.get('ratingValue', {})
#             if name and price:
#                 yield {"name": name, "price": f"{price:.2f} zł", "rating": rating}
#     except json.JSONDecodeError:
#         return
def extract_product_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    script_tag = soup.find('script', type='application/ld+json')
    if not script_tag:
        return

    try:
        data = json.loads(script_tag.string)
        for item in data.get('itemListElement', []):
            product = item.get('item', {})
            name = product.get('name')
            price = product.get('offers', {}).get('lowPrice')

            rating_info = product.get('aggregateRating', {})
            rating = rating_info.get('ratingValue')
            review_count = rating_info.get('reviewCount')

            if name and price:
                yield {
                    "name": name,
                    "price": f"{price:.2f} zł",
                    "rating": float(rating) if rating else 0,
                    "review_count": int(review_count) if review_count else 0
                }
    except json.JSONDecodeError:
        return

