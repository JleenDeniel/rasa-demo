import sqlite3

connection = sqlite3.connect('bank_data.db')
cursor = connection.cursor()


class User:
    name = ""
    email = ""

    def __init__(self, name, email):
        self.name = name
        self.email = email

    @staticmethod
    def add_user(name, email):
        res = cursor.execute("Insert into users (name, email) values "
                             "('{name}', '{email}')".format(name=name, email=email))
        if res is not None:
            Error("Insert in db error (error while adding new user)")

    @staticmethod
    def get_user_debit_balance(name="", email="") -> str:
        if name != "":
            res = cursor.execute("select balance from debit_cards where id == "
                                 "(select id_user from users where users.name == '{name}')".format(name=name))
        elif email != "":
            res = cursor.execute("select balance from debit_cards where id == "
                                 "(select id_user from users where users.email == '{email}')".format(email=email))
        else:
            Error("smth wrong with parameters while calling get_user_debit_balance")
        return res.fetchone()[0]

    @staticmethod
    def get_user_credit_balance(name="", email="") -> str:
        if name != "":
            res = cursor.execute("select balance from credit_cards where id == "
                                 "(select id_user from users where users.name == '{name}')".format(name=name))
        elif email != "":
            res = cursor.execute("select balance from credit_cards where id == "
                                 "(select id_user from users where users.email == '{email}')".format(email=email))
        else:
            Error("smth wrong with parameters while calling get_user_credit_balance")
        return res.fetchone()[0]


