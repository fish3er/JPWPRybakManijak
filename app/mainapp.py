from app import WebsiteIterator, extract_product_data
from filtry import filter_by_price_range
def main():
    base_url = "https://www.ceneo.pl/Ekspresy_do_kawy"
    scraper = WebsiteIterator(base_url, max_pages=5)

    # for page_html in scraper:
    #     for product in extract_product_data(page_html):
    #         print(f"{product['name']} - {product['price']}")

    print("Ekspresy taniej niż 1500 zł:")
    for page_html in scraper:
        for product in extract_product_data(page_html):
            filtered_product = filter_by_price_range(
                product,
                min_price=0,
                max_price=1500
            )
            if filtered_product:
                print(f"{filtered_product['name']} - {filtered_product['price']}")

if __name__ == "__main__":
    main()
