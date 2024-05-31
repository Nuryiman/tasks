class Book:
    def __init__(self, name_pm, autor_pm, page_pm):
        self.name = name_pm
        self.autor = autor_pm
        self.page = page_pm

    def info(self):
        information = f"название: {self.name}, автор: {self.autor}, кол. страниц: {self.page}"
        return information


book_not_comfort = Book('выйди из зоны комфорта', 'Брайан Трейси', 144)
book_by_best_you = Book('Будь лучшей версией себя', 'Дэн Вальдшмидт', 208)

b1 = book_by_best_you.info()

print(b1)
