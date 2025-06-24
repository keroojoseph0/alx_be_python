class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

class  Library:
    books = []

    def add_book(self, book):
        self.book = book
        self.books.append(self.book)

    def list_books(self):
        for book in self.books:
            class_name = book.__class__.__name__
            if class_name == "Book":
                print(f"{class_name}: {book.title} by {book.author}")
            
            elif class_name == "EBook":
                print(f"{class_name}: {book.title} by {book.author}, File Size: {book.file_size}KB")
            else:
                print(f"{class_name}: {book.title} by {book.author}, Page Count: {book.page_count}")
    
    def __str__(self):
        result = "Library Contents:\n"
        for book in self.books:
            class_name = book.__class__.__name__
            if class_name == "Book":
                result += f"{class_name}: {book.title} by {book.author}\n"
            elif class_name == "EBook":
                result += f"{class_name}: {book.title} by {book.author}, File Size: {book.file_size}KB\n"
            else:
                result += f"{class_name}: {book.title} by {book.author}, Page Count: {book.page_count}\n"
        return result.strip()
