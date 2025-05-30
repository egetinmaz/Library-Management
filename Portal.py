import tkinter as tk
from tkinter import messagebox
from Library_Management import Book, User, Library

def start_portal(library):
    window = tk.Tk()
    window.title("Library Management System")
    window.geometry("400x500")

    # --- Title ---
    tk.Label(window, text="Library Management System", font=("Helvetica", 16, "bold")).pack(pady=10)

    # --- Book Fields ---
    tk.Label(window, text="Book ISBN").pack()
    isbn_entry = tk.Entry(window)
    isbn_entry.pack(pady=5)

    tk.Label(window, text="Book Title").pack()
    title_entry = tk.Entry(window)
    title_entry.pack(pady=5)

    tk.Label(window, text="Book Author").pack()
    author_entry = tk.Entry(window)
    author_entry.pack(pady=5)

    # --- User Fields ---
    tk.Label(window, text="User ID").pack()
    user_id_entry = tk.Entry(window)
    user_id_entry.pack(pady=5)

    tk.Label(window, text="User Name").pack()
    user_name_entry = tk.Entry(window)
    user_name_entry.pack(pady=5)

    # --- Actions ---
    def add_book():
        title = title_entry.get()
        author = author_entry.get()
        isbn = isbn_entry.get()
        if not (title and author and isbn):
            messagebox.showerror("Error", "All book fields are required.")
            return
        library.add_book(Book(title, author, isbn))
        messagebox.showinfo("Success", f"Book '{title}' added!")

    def add_user():
        user_id = user_id_entry.get()
        name = user_name_entry.get()
        if not (user_id and name):
            messagebox.showerror("Error", "Both user fields are required.")
            return
        library.add_user(User(user_id, name))
        messagebox.showinfo("Success", f"User '{name}' added!")

    def borrow_book():
        isbn = isbn_entry.get()
        user_id = user_id_entry.get()
        result = library.borrow_book(isbn, user_id)
        messagebox.showinfo("Result", result)

    def return_book():
        isbn = isbn_entry.get()
        user_id = user_id_entry.get()
        result = library.return_book(isbn, user_id)
        messagebox.showinfo("Result", result)

    # --- Buttons ---
    tk.Button(window, text="Add Book", command=add_book).pack(pady=5)
    tk.Button(window, text="Add User", command=add_user).pack(pady=5)
    tk.Button(window, text="Borrow Book", command=borrow_book).pack(pady=5)
    tk.Button(window, text="Return Book", command=return_book).pack(pady=5)

    window.mainloop()

if __name__ == "__main__":
    my_library = Library("City Library")
    start_portal(my_library)
