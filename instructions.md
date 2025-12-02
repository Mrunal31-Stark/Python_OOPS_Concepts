# Simple Library Management (OOP) — Project

A small Python project that demonstrates core Object-Oriented Programming concepts: **encapsulation**, **inheritance**, **polymorphism**, and **abstraction**. It's intentionally compact so you can read, run, and extend it quickly.

---

## Files included

- `models.py` — classes and OOP logic (Book, User, Member, Librarian, Library)
- `main.py` — simple CLI demo to interact with the library
- `instructions.md` — (this file) explains setup, how OOP concepts map to the code, and extension ideas

---

## Project overview

This mini-project simulates a library where users (Members) can borrow and return books, and a Librarian can add or remove books. The code uses:

- **Encapsulation**: internal state like `_available_copies` is kept private-ish and accessed via methods.
- **Inheritance**: `Member` and `Librarian` inherit from `User`.
- **Polymorphism**: both `Member` and `Librarian` implement `get_role()` differently and `__str__`/`info()` variations.
- **Abstraction**: an abstract base `User` (via `abc.ABC`) defines required methods.


## How to run

1. Make sure you have Python 3.8+ installed.
2. Save `models.py` and `main.py` in the same folder.
3. Run:

```bash
python main.py
```

You should see printed output that demonstrates borrowing, returning, and book counts changing, illustrating encapsulation and behavior.

---

## OOP concept mapping (quick)

- **Encapsulation**: `_available_copies` and `_books` are internal; access via methods `borrow()`, `returned()`, `find_book()`.
- **Inheritance**: `Member` and `Librarian` extend `User` and implement `get_role()`.
- **Polymorphism**: `get_role()` returns different strings; both user classes provide different capabilities.
- **Abstraction**: `User` is an abstract base class requiring `get_role()` to be implemented.

---

## Extensions (ideas for practice)

- Persist data to a JSON or SQLite file.
- Add due dates and overdue fines.
- Add search by title/author (not only ISBN).
- Enforce authentication & session (simple username/password for Librarian).
- Add unit tests covering borrow/return edge cases.

---


