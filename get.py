from library import Book, BookService

book = BookService()

book_services = Book(title= "Арсен Люпен", author='Морис Леблан')

# book.add_book(book_services)

find = book.find_book_by_id('1')
if find:
    print(f"Book is found: {find.title}, {find.author}")

# delete = book.delete_book_by_id(12)

book.list_books()
