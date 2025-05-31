import streamlit as st
from Library_Management import Book, User, Library

# Initialize the library object
if "library" not in st.session_state:
    st.session_state.library = Library("City Library")

library = st.session_state.library

st.title("📚 Library Management System")

# --- Book Fields ---
st.subheader("Book Information")
isbn = st.text_input("Book ISBN")
title = st.text_input("Book Title")
author = st.text_input("Book Author")

# --- User Fields ---
st.subheader("User Information")
user_id = st.text_input("User ID")
user_name = st.text_input("User Name")

# --- Actions ---
col1, col2 = st.columns(2)

with col1:
    if st.button("➕ Add Book"):
        if not (isbn and title and author):
            st.error("All book fields are required.")
        else:
            library.add_book(Book(title, author, isbn))
            st.success(f"Book '{title}' added!")

    if st.button("👤 Add User"):
        if not (user_id and user_name):
            st.error("Both user fields are required.")
        else:
            library.add_user(User(user_id, user_name))
            st.success(f"User '{user_name}' added!")

with col2:
    if st.button("📖 Borrow Book"):
        if not (isbn and user_id):
            st.error("ISBN and User ID are required to borrow.")
        else:
            result = library.borrow_book(isbn, user_id)
            st.info(result)

    if st.button("🔁 Return Book"):
        if not (isbn and user_id):
            st.error("ISBN and User ID are required to return.")
        else:
            result = library.return_book(isbn, user_id)
            st.info(result)

# Optional: Show current books/users
with st.expander("📚 View All Books"):
    st.write(library.books)

with st.expander("👥 View All Users"):
    st.write(library.users)
