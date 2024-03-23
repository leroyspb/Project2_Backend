users_list = []

class User:

    def __init__(self, login, password):
        self.login = login
        self.password = password

user1 = User(login="user@mail.ru", password="1234")
user2 = User(login="user@yandex.ru", password="qwerty")
user3 = User(login="user@gmail.com", password="12qw")

users_list.append(user1)
users_list.append(user2)
users_list.append(user3)

for user in users_list:
    print(user.login)