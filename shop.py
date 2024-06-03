from user import User
from product import Product
from payment import Payment
from order import Order

"""Определяем класс Shop, который описывает работу кадрового агентства"""
class Shop:
    def __init__(self, shop_id: int):
        """
        Инициализация объекта магазин.
        """
        self.shop_id = shop_id
        self.users = []
        self.products = []
        self.payments = []
        self.orders = []

    def add_user(self, user: User):
        """
        Добавление пользователяв в список доступных пользователей.
        """
        self.users.append(user)

    def add_product(self, product: Product):
        """
        Добавление товара в список доступных товаров.
        """
        self.products.append(product)

    def add_payment(self, payment: Payment):
        """
        Добавление информации об оплате в список существующей информации об оплате.
        """
        self.payments.append(payment)

    def add_order(self, order: Order):
        """
        Добавление заказа в список доступных заказов.
        """
        self.orders.append(order)

    def __str__(self):
        return f"Shop ID: {self.shop_id}, User: {len(self.users)}, Product: {len(self.products)}, Payment: {len(self.payments)}, Order: {len(self.orders)}"


    def read_users(self, users_fname):
        with open(users_fname, "r") as users_f:
            for line in users_f:
                buyer_id, name, date, tel, email, pol = line.split(";")
                buyer_id = int(buyer_id)
                name = str(name)
                date = str(date)
                tel = int(tel)
                email = str(email)
                pol = str(pol)
                user = User(buyer_id, name, date, tel, email, pol)
                self.users.append(user)

    def read_payments(self, payments_fname):
        with open(payments_fname, "r") as payments_f:
            for line in payments_f:
                payment_id, buyer_id, product_id, price, date, status = line.split(";")
                product_id = int(product_id)
                buyer_id = int(buyer_id)
                product_id = int(product_id)
                price = int(price)
                date = str(date)
                status = str(status)
                payment = Payment(payment_id, buyer_id, product_id, price, date, status)
                self.payments.append(payment)

    def read_products(self, products_fname):
        with open(products_fname, "r") as products_f:
            for line in products_f:
                product_id, categori, color, size, producer, price = line.split(";")
                product_id = int(product_id)
                categori = str(categori)
                color = str(color)
                size = int(size)
                producer = str(producer)
                price = int(price)
                product = Product(product_id, categori, color, size, producer, price)
                self.products.append(product)

    def read_orders(self, orders_fname):
        with open(orders_fname, "r") as orders_f:
            for line in orders_f:
                order_id, buyer_id, product_id, price, date, status = line.split(";")
                order_id = int(order_id)
                buyer_id = int(buyer_id)
                product_id = int(product_id)
                price = int(price)
                date = str(date)
                status = str(status)
                order = Order(order_id, buyer_id, product_id, price, date, status)
                self.orders.append(order)

if __name__ == '__main__':
    """
    Создайте список для хранения доставленных заказов
    """
    delivered_orders = []

    with open("order.txt", "r", encoding="utf-8") as orders_f:
        for line in orders_f:
            order_id, buyer_id, product_id, price, date, status = line.split(";")
            status = status.strip()  # Уберем лишние пробелы
            if status == "доставлен":
                order = Order(int(order_id), int(buyer_id), int(product_id), int(price), date, status)
                delivered_orders.append(order)

    # Вывод всех заказов с статусом "доставлен"
    for order in delivered_orders:
        print(order)