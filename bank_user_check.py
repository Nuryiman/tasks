class Person:
    def __init__(self, name_pm: str, language_pm: str):
        self.name = name_pm
        self.language = language_pm

    def introduce(self):
        if self.language == 'ru':
            print(f'Привет меня зовут {self.name}')
        elif self.language == 'en':
            print(f'Hello, my name is {self.name}')
        elif self.language == 'kg':
            print(f'Салам, менин атым {self.name}')
        else:
            print(f'Hello, my name is {self.name}')


class BankAccount(Person):
    def __init__(self, name_pm: str, language_pm: str, account_number_pm: int, balance_pm: int):
        self.name = name_pm
        self.language = language_pm
        self.account_number = account_number_pm
        self.balance = {self.account_number: balance_pm}

    def deposit(self, amount: int):
        self.balance[self.account_number] += amount

    def withdraw(self, amount: int):
        self.balance[self.account_number] -= amount


p1 = Person('Nurbek', 'ru')
p2 = Person('Beka', 'kaskj')
bank_p1 = BankAccount('Nurbek', 'ru', 10, 500_000)
bank_p2 = BankAccount('Beka', 'kg', 20, 1_000_000)
p2.introduce()
p1.introduce()
bank_p1.deposit(15000)
print(bank_p1.balance)
print(bank_p2.balance)
bank_p2.withdraw(200_000)
print(bank_p2.balance)

