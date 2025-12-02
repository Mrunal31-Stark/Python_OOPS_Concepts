from models import Book, Library, Member, Librarian

def demo():
lib = Library("Central Library")


# librarian sets up the library
libby = Librarian("L1", "Anita")
libby.add_book(lib, Book("978-1", "Python 101", "Jake", copies=2))
libby.add_book(lib, Book("978-2", "Clean Code", "Robert", copies=1))


# members
alice = Member("M1", "Alice")
bob = Member("M2", "Bob", max_books=2)


print(lib)
print("\n-- Borrow attempts --")
alice.borrow_book(lib, "978-1")
bob.borrow_book(lib, "978-1")
bob.borrow_book(lib, "978-1") # third attempt should fail if no copies left


print("\nAfter borrowing:\n")
print(lib)


print("\n-- Returns --")
alice.return_book(lib, "978-1")
print(lib)


print("\n-- Librarian removes a book --")
libby.remove_book(lib, "978-2")
print(lib)




if __name__ == "__main__":
demo()
