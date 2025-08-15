# True means available
# False means borrowed or missing.

import json
import os

Data_File = "library_dataa.json"

def load_data():
    if not os.path.exists(Data_File):

        return {
            "Harry Potter": {"author": "J.K. Rowling", "available": True},
            "Atomic Habits": {"author": "James Clear", "available": True},
            "The Alchemist": {"author": "Paulo Coelho", "available": True}
        } 
    with open(Data_File,"r")as f:
        return json.load(f) 
    
def save_data(library):
    with open(Data_File,"w")as f:
        json.dump(library,f,indent=2,ensure_ascii=False)


def Add_book(library):
    name = input("Enter the name of the book : ")
    
    if name in library:
        print("Already Exist!")
        return
    author = input("Enter the name of the author : ").strip() or "unknown"
    library[name] = {"author": author,"available":True}
    save_data(library)
    print(f"{name} by {author} added sucessfully and marked available")


def view_available_books(library):
    print("All Books")
    found = False

    for title,info in library.items():
        if info.get("available",False):
            print(f"-{title} by {info.get('author','unknown')}")
            found = True

    if not found:
        print("No books are currently available.")

def  View_available_books_with_status(library):
    print("Available Books")
    if not library:
        print("Library is empty")
        return
    for book,info in library.items():
        status = "Available" if info.get("available",False) else "borrow"
        print(f"-{book} by {info.get('author')} [{status}]")

def borrow_a_book(library):
    name = input("Enter the name of the book you want to borrow : ").lower()

    if name not in library:
        print("Book not found")
        return
    if not library[name].get("available",False):
        print("Sorry this book is already Borrowed.")
        return
    else:
        print("You have sucessfully borrwed a book")
        library[name]["available"] = False
        save_data(library)

def return_a_book(library):
    name = input("Enter the name of the book you want to return : ")
    if name not in library:
        print("Book Not Found!")
        return
    if name in library:
        print("The book has sucessfully returned")
        library[name]["available"] = True
    save_data(library)


def search_a_book(library):
    keyword = input("Enter the name of the book : ").strip().lower()
    matches = []

    for title,info in library.items():
        if keyword in title.lower():
            matches.append((title,info))
    if not matches:
        print("No result Found.")
        return
    print("\n Search result.")
    for title,info in matches:
        status = "Available" if info.get("available",False) else "borrow"
        print(f"-{title} by {info.get('author','unknown')} [{status}]")
        
def remove_a_book(library):
    name = input("Enter the book you want to remove : ").strip()

    if name not in library:
        print("Book not Found")
        return
    
    conform = input(f"Are you sure you want to remove '{name}'? (Y/N) : ").strip().lower()

    if conform == "y":
        del library[name]
        save_data(library)
        print(f"{name} removed from the library.")
    else:
        print("Canceled. No changes made.")

def Exit(library):
    print("Goodbye.....")
    

def main():
    library = load_data()
    print("Welcome To The Libreary Management System")

    while True:
           

        print("\n--- Library Menu ---")
        print("1. Add a book")
        print("2. View available books")
        print("3. View all books (with status)")
        print("4. Borrow a book")
        print("5. Return a book")
        print("6. Search by title")
        print("7. Remove a book (admin)")
        print("8. Exit")

        choice = int(input("Enter choice (1-8): "))

        if choice == 1:
            Add_book(library)
        elif choice == 2:
            view_available_books(library)
        elif choice == 3:
            View_available_books_with_status(library)
        elif choice == 4:
            borrow_a_book(library)
        elif choice == 5:
            return_a_book(library)
        elif choice == 6:
            search_a_book(library)
        elif choice == 7:
            remove_a_book(library)
        elif choice == 8:
            Exit(library)
        else:
            print("Invalid Number Entered")

if __name__=="__main__":
    main()



