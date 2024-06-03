class Product:
    def __init__(self, product_id, categori, color, size, producer, price):
        self.product_id = product_id
        self.categori = categori
        self.color = color
        self.size = size
        self.producer = producer
        self.price = price

    def __str__(self):
        return f"{self.product_id}, {self.categori}, {self.color}, {self.size}, {self.producer}, {self.price}"

if __name__ == '__main__':
    products = []
    with open("product.txt", "r", encoding="utf-8") as products_f:
        for line in products_f:
            product_id, categori, color, size, producer, price = line.split(";")
            product_id = int(product_id)
            categori = str(categori)
            color = str(color)
            size = int(size)
            producer = str(producer)
            price = int(price)
            product = Product(product_id, categori, color, size, producer, price)
            products.append(product)
    with open("product_sorted.txt", "w", encoding="utf-8") as products_sorted_f:
        products_sorted_f.write("product_id, categori, color, size, producer, price\n")
        for product in sorted(products, key=lambda x: x.price, reverse=True):
            products_sorted_f.write(str(product)+"\n")
