from abc import ABC, abstractmethod
from typing import List


class Book:
def __init__(self, isbn: str, title: str, author: str, copies: int = 1):
self.isbn = isbn
self.title = title
self.author = author
self._available_copies = copies # encapsulated attribute


def borrow(self) -> bool:
"""Attempt to borrow a book. Returns True if successful."""
if self._available_copies > 0:
self._available_copies -= 1
return True
return False


def returned(self):
self._available_copies += 1


def available(self) -> int:
return self._available_copies


def __str__(self):
return f"{self.title} by {self.author} (ISBN: {self.isbn}) - Available: {self._available_copies}"




class User(ABC):
def __init__(self, user_id: str, name: str):
self.user_id = user_id
self.name = name


@abstractmethod
def get_role(self) -> str:
pass


def info(self) -> str:
return f"{self.name} (ID: {self.user_id}) - {self.get_role()}"




class Member(User):
def __init__(self, user_id: str, name: str, max_books: int = 3):
super().__init__(user_id, name)
self._borrowed: List[str] = [] # store ISBNs
self.max_books = max_books


def get_role(self) -> str:
return "Member"


def borrow_book(self, library, isbn: str) -> bool:
if len(self._borrowed) >= self.max_books:
print(f"{self.name} reached borrow limit ({self.max_books}).")
return False
book = library.find_book(isbn)
if not book:
print("Book not found in library.")
return False
if book.borrow():
self._borrowed.append(isbn)
print(f"{self.name} successfully borrowed '{book.title}'.")
return True
return "\n".join(lines)
