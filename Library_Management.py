class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        self.borrower = None

    def __str__(self):
        status = "Available" if self.available else f"Borrowed by {self.borrower.name}"
        return f"📖 '{self.title}' by {self.author} (ISBN: {self.isbn}) - {status}"

    def __repr__(self):
        return self.__str__()


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.books_borrowed = []

    def __str__(self):
        books = ", ".join(book.title for book in self.books_borrowed) or "No books borrowed"
        return f"👤 {self.name} (ID: {self.user_id}) - {books}"

    def __repr__(self):
        return self.__str__()

    def return_all_books(self):
        return_count = len(self.books_borrowed)
        for book in self.books_borrowed[:]:
            book.available = True
            book.borrower = None
            self.books_borrowed.remove(book)
        return return_count


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def borrow_book(self, book_isbn, user_id):
        book = next((b for b in self.books if b.isbn == book_isbn), None)
        user = next((u for u in self.users if u.user_id == user_id), None)

        if not book:
            return "❌ Book not found."
        if not user:
            return "❌ User not found."
        if not book.available:
            return f"❌ Book '{book.title}' is currently unavailable."

        book.available = False
        book.borrower = user
        user.books_borrowed.append(book)
        return f"✅ '{book.title}' has been borrowed by {user.name}."

    def return_book(self, book_isbn, user_id):
        book = next((b for b in self.books if b.isbn == book_isbn), None)
        user = next((u for u in self.users if u.user_id == user_id), None)

        if not book:
            return "❌ Book not found."
        if not user:
            return "❌ User not found."
        if book.available or book.borrower != user:
            return "⚠️ This book was not borrowed by this user."

        book.available = True
        book.borrower = None
        user.books_borrowed.remove(book)
        return f"✅ '{book.title}' has been returned by {user.name}."

    def __str__(self):
        return f"🏛️ {self.name} Library — {len(self.books)} books, {len(self.users)} users"

    def __repr__(self):
        return self.__str__()
