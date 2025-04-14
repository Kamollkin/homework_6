class Book:
    def __init__(self, avtor, book_name, year):
        self.avtor = avtor
        self.book_name = book_name
        self.year = year
    def info(self):
        print(f"Автор - {self.avtor}, Название - {self.book_name}, Год выпуска - {self.year}")

book = Book("Агата Кристи", "Десять негритят", "1939")
book.info()