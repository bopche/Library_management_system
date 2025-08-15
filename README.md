Library Management System

This is a simple Library Management System I built using Python.
It runs in the terminal and allows me (or anyone using it) to manage books easily — whether it's adding new ones, borrowing, returning, or even removing them.

The project uses JSON file storage, so the data (like book titles, authors, and availability status) is saved even after closing the program. That means the library keeps growing and remembering changes over time.

Features

Add new books with title and author.

View available books only, or see all books with their status.

Borrow and return books (availability updates automatically).

Search for books by title (case-insensitive).

Remove books from the library (admin action).

Data is stored persistently in a JSON file.

How it works

When the program starts, it loads books from a JSON file (or creates a few sample books if no file exists).

Every change — like adding, borrowing, or returning — is immediately saved so nothing gets lost.

The menu-driven interface makes it simple to navigate and use.

📌 Why I built this

I made this project to practice Python basics like functions, file handling, JSON operations, loops, and conditional logic.
It’s small but practical — a perfect step toward building more complex data management systems in the future.
