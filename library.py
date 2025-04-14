from HW2_6 import Library
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        

class BookService:
    def __init__(self):
        self.db = Library()

    def add_book(self,book):
        self.db.add_book(book)
        print("A book is successfully added!")

    def find_book_by_id(self,id):
        book_data = self.db.get_book(id)
        if book_data:
            return Book(title=book_data[1], author=book_data[2])
        else:
            print("Book is not found!")
    
        
    def delete_book_by_id(self,id):
        delete_book = self.find_book_by_id(id)
        if delete_book:
            self.db.delete_book_by_id(id)
        else:
            None

    def list_books(self):
        self.db.list_books()

