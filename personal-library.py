import json
import os

LIBRARY_FILE = 'library.txt'


def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, 'r', encoding='utf-8') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []


def save_library(library):
    with open(LIBRARY_FILE, 'w', encoding='utf-8') as file:
        json.dump(library, file, indent=4)


def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")

    while True:
        try:
            year = int(input("Enter the publication year: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number for the year.")

    genre = input("Enter the genre: ")
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read_status = read_input == "yes"

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }
    library.append(book)
    print("Book added successfully!")


def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found.")


def search_books(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ").strip()
    if choice == '1':
        term = input("Enter the title: ").strip().lower()
        matches = [book for book in library if term in book["title"].lower()]
    elif choice == '2':
        term = input("Enter the author: ").strip().lower()
        matches = [book for book in library if term in book["author"].lower()]
    else:
        print("Invalid choice.")
        return

    if matches:
        print("Matching Books:")
        for i, book in enumerate(matches, start=1):
            read_status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    else:
        print("No matching books found.")


def display_books(library):
    if not library:
        print("Your library is empty.")
        return
    print("Your Library:")
    for i, book in enumerate(library, start=1):
        read_status = "Read" if book["read"] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")


def display_statistics(library):
    total_books = len(library)
    if total_books == 0:
        print("No books in the library.")
        return
    read_books = sum(book["read"] for book in library)
    percent_read = (read_books / total_books) * 100
    print(f"Total books: {total_books}")
    print(f"Books read: {read_books}")
    print(f"Percentage read: {percent_read:.1f}%")


def main():
    library = load_library()

    while True:
        print("\nMenu")
        print("Welcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_books(library)
        elif choice == '4':
            display_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
