from user import User
from product import Product

class Order:
    """

    """
    def __init__(self, order_id: int, buyer_id: int, product_id: int, price: int, date: str, status: str):

        self.order_id = order_id
        self.buyer_id = buyer_id
        self.product_id = product_id
        self.price = price                                                                                           
        self.date = date
        self.status = status
    def __str__(self):
        return f"{self.order_id}, {self.buyer_id}, {self.product_id}, {self.price}, {self.date}, {self.status}"

if __name__ == '__main__':
    orders = []
    with open("order.txt", "r", encoding="utf-8") as orders_f:
        for line in orders_f:
            order_id, buyer_id, product_id, price, date, status = line.split(";")
            order_id = int(order_id)
            buyer_id = int(buyer_id)
            product_id = int(product_id)
            price = int(price)
            date = str(date)
            status = str(status)
            order = Order(order_id, buyer_id, product_id, price, date, status)
            orders.append(order)
    with open("order_sorted.txt", "w", encoding="utf-8") as orders_sorted_f:
        orders_sorted_f.write("order_id, buyer_id, product_id, price, date, status\n")
        for order in sorted(orders, key=lambda x: x.date, reverse=True):
            orders_sorted_f.write(str(order)+"\n")



