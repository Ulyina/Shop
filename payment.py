class Payment:
    def __init__(self, payment_id, buyer_id, product_id, price, date, status):
        self.payment_id = payment_id
        self.buyer_id = buyer_id
        self.product_id = product_id
        self.price = price
        self.date = date
        self.status = status

    def __str__(self):
        return f"{self.payment_id}, {self.buyer_id}, {self.product_id}, {self.price}, {self.date}, {self.status}"

if __name__ == '__main__':
    payments = []
    with open("payment.txt", "r", encoding="utf-8") as payments_f:
        for line in payments_f:
            payment_id, buyer_id, product_id, price, date, status = line.split(";")
            product_id = int(product_id)
            buyer_id = int(buyer_id)
            product_id = int(product_id)
            price = int(price)
            date = str(date)
            status = str(status)
            payment = Payment(payment_id, buyer_id, product_id, price, date, status)
            payments.append(payment)
    with open("payment_sorted.txt", "w", encoding="utf-8") as payments_sorted_f:
        payments_sorted_f.write("payment_id, buyer_id, product_id, price, date, status\n")
        for payment in sorted(payments, key=lambda x: x.date, reverse=True):
            payments_sorted_f.write(str(payment)+"\n")