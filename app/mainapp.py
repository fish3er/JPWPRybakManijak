from app import WebsiteIterator, extract_product_data

def main():
    base_url = "https://www.ceneo.pl/Ekspresy_do_kawy"
    scraper = WebsiteIterator(base_url, max_pages=10)

    for page_html in scraper:
        for product in extract_product_data(page_html):
            print(f"{product['name']} - {product['price']}")

if __name__ == "__main__":
    main()
