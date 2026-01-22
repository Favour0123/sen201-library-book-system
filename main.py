class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def display_books(self):
        print("Available Books")
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}")


def main():
    library = Library()

    library.add_book("Python Programming", "John Doe")
    library.add_book("Software Engineering", "Jane Smith")

    library.display_books()


if __name__ == "__main__":
    main()
