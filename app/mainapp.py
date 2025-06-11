from control import append

from app import WebsiteIterator, extract_product_data
from filtry import filter_by_price_range, filter_by_rating, filter_by_review_count
from savetocsv import save_to_csv
def main():
    base_url = "https://www.ceneo.pl/Ekspresy_do_kawy"
    scraper = WebsiteIterator(base_url, max_pages=10)
    # print(next(scraper))
    # for page_html in scraper:
    #     for product in extract_product_data(page_html):
    #         print(product)
    # for page_html in scraper:
    #     for product in extract_product_data(page_html):
    #         print(f"{product['name']} - {product['price']}")

    # print("Ekspresy taniej niż 1500 zł:")
    # for page_html in scraper:
    #     for product in extract_product_data(page_html):
    #         filtered_product = filter_by_price_range(
    #             product,
    #             min_price=200,
    #             max_price=1500
    #         )
    #         if filtered_product:
    #             print(f"{filtered_product['name']} - {filtered_product['price']}")
    result= []
    for page_html in scraper:
        for product in extract_product_data(page_html):
            filtered_product = filter_by_rating(
                product,
                min_rating=4
            )
            if filtered_product:
                # print(f"{filtered_product['name']} - {filtered_product['price']} - Rating: {filtered_product['rating'] } przy {filtered_product['review_count']} opiniach" )
                result.append(filtered_product)
    result.sort(key=lambda product: product['rating'], reverse=True)

    final = []
    for i in range(len(result)):
        if result[i] is not None:
            filtered_product = result[i]
            if filtered_product['review_count'] > 40:
                if filtered_product not in final:
                    final.append(filtered_product)
    for i in range(len(final)):
        print(f"{final[i]['name']} - {final[i]['price']} - Rating: {final[i]['rating'] } przy {final[i]['review_count']} opiniach" )

    # result = []
    # for page_html in scraper:
    #     for product in extract_product_data(page_html):
    #         filtered_product = filter_by_review_count(
    #             product,
    #             min_review=100
    #         )
    #         if filtered_product:
    #             result.append(filtered_product)
    #             print(f"{filtered_product['name']} - {filtered_product['price']} - Rating: {filtered_product['rating'] } przy {filtered_product['review_count']} opiniach" )
    save_to_csv(result)

if __name__ == "__main__":
    main()
