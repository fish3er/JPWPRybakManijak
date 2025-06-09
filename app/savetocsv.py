import csv

def save_to_csv(products, filename="products.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "price", "rating", "review_count"])
        writer.writeheader()
        writer.writerows(products)