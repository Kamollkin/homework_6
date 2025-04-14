import sqlite3

class Library:

    def __init__(self, db_name="library.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
             CREATE TABLE IF NOT EXISTS books(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 title TEXT,
                 author TEXT         
       )  
                                         
    """)
        

        
    def add_book(self,book):
        self.cursor.execute("INSERT INTO books(title, author)VALUES (?, ?)", (book.title, book.author))
        self.connection.commit()

    def get_book(self,id):
        self.cursor.execute("SELECT * FROM books WHERE id = ?", (id,))
        return self.cursor.fetchone()
    
    def delete_book_by_id(self,id):
        self.cursor.execute("DELETE FROM books WHERE id= ?", (id,))
        self.connection.commit()
        print(f"Book with id {id} was deleted")

    def list_books(self):
        self.cursor.execute("SELECT * FROM books")
        books = self.cursor.fetchall()
        print(books)

