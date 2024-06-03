class User:
    def __init__(self, buyer_id, name, date, tel, email, pol):
        self.buyer_id = buyer_id
        self.name = name
        self.date = date
        self.tel = tel
        self.email = email
        self.pol = pol
    def __str__(self):
        return f"{self.buyer_id}, {self.name}, {self.date}, {self.tel}, {self.email}, {self.pol}"
    
if __name__ == '__main__':
    users = []
    with open("user.txt", "r", encoding="utf-8") as users_f:
        for line in users_f:
            buyer_id, name, date, tel, email, pol = line.split(";")
            buyer_id = int(buyer_id)
            name = str(name)
            date = str(date)
            tel = int(tel)
            email = str(email)
            pol = str(pol)
            user = User(buyer_id, name, date, tel, email, pol)
            users.append(user)
    with open("user_sorted.txt", "w", encoding="utf-8") as users_sorted_f:
        users_sorted_f.write("buyer_id, name, date, tel, email, pol\n")
        for user in sorted(users, key=lambda x: x.date, reverse=True):
            users_sorted_f.write(str(user)+"\n")
