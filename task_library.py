"""
Создайте класс Book с атрибутами title (название), author (автор) .
 И с методом display_info который печатает всю информацию по книге

Создайте класс Library, который будет содержать список книг в атрибуте books.
В классе Library реализуйте методы add_book(), remove_book(),
find_book_by_title(), find_book_by_author(), и list_books().
"""


class Book:
    def __init__(self, title_pm, author_pm):
        self.title = title_pm
        self.author = author_pm

    def display_info(self):
        print(f'Название: {self.title}, Автор: {self.author}')


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, new_book: Book):
        self.books.append(new_book)

    def remove_book(self, rm_book: Book):
        if rm_book in self.books:
            self.books.remove(rm_book)

    def find_book_by_title(self, book_title: str):
        for item in self.books:
            if item.title == book_title:
                return item

    def find_book_by_author(self, book_author: str):
        for item in self.books:
            if item.author == book_author:
                return item.title

    def list_books(self):
        return self.books


b1 = Book('Узак жол', 'Мукай Элебаев')
b2 = Book('До встречи с тобой', 'Джоджо Мойес')
l1 = Library()
l1.add_book(b1)
print(l1.list_books())

l1.add_book(b2)
l1.remove_book(b1)
print(l1.list_books())

l1.find_book_by_title('Узак жол')

print(l1.find_book_by_author('Джоджо Мойес'))
# l1.find_book_by_title(b2)
# l1.find_book_by_author(b2)
