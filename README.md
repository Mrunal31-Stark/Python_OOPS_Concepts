# Python OOP Concepts - Complete Guide
## Polymorphism, Inheritance, Encapsulation & Abstraction


```
Polymorphism = Ek interface, bahut tarah ke objects ko handle karna.
Ek hi naam ka method, alag-alag classes में alag-alag kaam kar sakta hai.
```

---

### Inheritance क्या है?

Inheritance का मतलब है - कुछ चीजें एक parent class से child class में आती हैं, जैसे genes।

```
Inheritance = Child class, Parent class के properties को ले सकती है
Code reusability - एक बार लिखो, बार-बार use करो
DRY principle = Don't Repeat Yourself
```

---

### Encapsulation क्या है?

Encapsulation = Data को hide करना। जैसे बैंक में आपके पैसे lock में रहते हैं।


```
Private data = [translate:__password]] = सिर्फ class के अंदर
Public methods = बाहर से access कर सकते हो
यह security देता है
```

---

### Abstraction क्या है?

Abstraction = सिर्फ जरूरी चीजें दिखाओ, बाकी को छुपाओ।


```
Abstract class = Template दे सकता है, लेकिन खुद काम नहीं कर सकता
Subclasses उस template को complete करती हैं
Complexity को hide करो, simplicity दिखाओ
```

---

## 🔧 PART 2: DETAILED TECHNICAL EXPLANATION WITH PYTHON CODE

### 1. POLYMORPHISM - The "Many Forms" Concept

Polymorphism दो types का होता है:
1. **Method Overriding** (Runtime Polymorphism)
2. **Duck Typing** (Dynamic Polymorphism)

#### Example 1: Method Overriding (Most Common)

```python
# Parent Class
class Animal:
    def speak(self):
        return "Some generic animal sound"
    
    def move(self):
        return "Moving..."

# Child Class 1
class Dog(Animal):
    def speak(self):  # Overriding parent method
        return "Woof! Woof!"
    
    def move(self):  # Overriding parent method
        return "Dog is running on 4 legs"

# Child Class 2
class Bird(Animal):
    def speak(self):  # Overriding parent method
        return "Tweet! Tweet!"
    
    def move(self):  # Overriding parent method
        return "Bird is flying"

# Child Class 3
class Fish(Animal):
    def speak(self):  # Overriding parent method
        return "Bubble sound"
    
    def move(self):  # Overriding parent method
        return "Fish is swimming"

# Polymorphic Behavior - Same method, different behavior
def make_animal_sound(animal):
    print(animal.speak())
    print(animal.move())
    print("-" * 40)

# Creating objects
dog = Dog()
bird = Bird()
fish = Fish()

# Same function works with different objects
make_animal_sound(dog)    # Calls Dog's speak() and move()
make_animal_sound(bird)   # Calls Bird's speak() and move()
make_animal_sound(fish)   # Calls Fish's speak() and move()

# Output:
# Woof! Woof!
# Dog is running on 4 legs
# ----------------------------------------
# Tweet! Tweet!
# Bird is flying
# ----------------------------------------
# Bubble sound
# Fish is swimming
# ----------------------------------------
```

#### Example 2: Duck Typing (Python's Unique Feature)

```python
# Notice: These classes don't inherit from same parent
# But they can be used together because they have same methods

class Guitar:
    def play(self):
        return "🎸 Guitar playing beautiful music..."
    
    def tune(self):
        return "Tuning guitar strings..."

class Violin:
    def play(self):
        return "🎻 Violin playing classical music..."
    
    def tune(self):
        return "Tuning violin strings..."

class Piano:
    def play(self):
        return "🎹 Piano playing melodious notes..."
    
    def tune(self):
        return "Tuning piano keys..."

# Function doesn't care about the type, just needs play() method
def perform_concert(instrument):
    print(instrument.play())
    print(instrument.tune())

# Creating objects
guitar = Guitar()
violin = Violin()
piano = Piano()

# All work with same function - THIS IS DUCK TYPING
# "If it has a play() method, treat it as a playable instrument"
perform_concert(guitar)
perform_concert(violin)
perform_concert(piano)

# Output:
# 🎸 Guitar playing beautiful music...
# Tuning guitar strings...
# 🎻 Violin playing classical music...
# Tuning violin strings...
# 🎹 Piano playing melodious notes...
# Tuning piano keys...
```

#### Example 3: Polymorphism with Built-in Functions

```python
# Python's built-in functions demonstrate polymorphism

# len() works with different types
print(len("Hello"))           # 5 (string length)
print(len([1, 2, 3, 4]))      # 4 (list length)
print(len({"a": 1, "b": 2}))  # 2 (dict length)

# str() converts different types
print(str(42))                # "42"
print(str([1, 2, 3]))         # "[1, 2, 3]"
print(str({"name": "Ali"}))   # "{'name': 'Ali'}"

# Example: Custom class with __len__
class Library:
    def __init__(self):
        self.books = ["Python 101", "Data Science", "Web Dev", "AI Basics"]
    
    def __len__(self):
        return len(self.books)
    
    def __str__(self):
        return f"Library with {len(self.books)} books"

lib = Library()
print(len(lib))      # 4 (uses our __len__ method)
print(str(lib))      # Library with 4 books
```

---

### 2. INHERITANCE - Code Reusability

Inheritance allows a class to inherit properties and methods from another class.

#### Example 1: Simple Inheritance

```python
# Parent Class
class Vehicle:
    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price
    
    def start_engine(self):
        return f"Engine started for {self.brand} {self.color} vehicle"
    
    def stop_engine(self):
        return "Engine stopped"
    
    def get_info(self):
        return f"Brand: {self.brand}, Color: {self.color}, Price: ${self.price}"

# Child Class 1
class Car(Vehicle):
    def __init__(self, brand, color, price, num_doors):
        super().__init__(brand, color, price)  # Call parent constructor
        self.num_doors = num_doors  # Car-specific property
    
    def get_info(self):
        parent_info = super().get_info()  # Call parent method
        return f"{parent_info}, Doors: {self.num_doors}"

# Child Class 2
class Motorcycle(Vehicle):
    def __init__(self, brand, color, price, has_sidecar):
        super().__init__(brand, color, price)
        self.has_sidecar = has_sidecar
    
    def start_engine(self):  # Override parent method
        return f"Motorcycle engine roars! {self.brand} is ready"

# Creating objects
car = Car("Toyota", "Blue", 25000, 4)
bike = Motorcycle("Harley", "Black", 15000, False)

print(car.start_engine())     # Engine started for Toyota Blue vehicle
print(car.get_info())         # Brand: Toyota, Color: Blue, Price: $25000, Doors: 4
print()
print(bike.start_engine())    # Motorcycle engine roars! Harley is ready
print(bike.get_info())        # Brand: Harley, Color: Black, Price: $15000
```

#### Example 2: Multi-level Inheritance

```python
# Grandparent Class
class LivingBeing:
    def breathe(self):
        return "Breathing..."
    
    def eat(self):
        return "Eating food..."

# Parent Class
class Animal(LivingBeing):
    def walk(self):
        return "Walking on legs..."

# Child Class
class Dog(Animal):
    def bark(self):
        return "Woof! Woof!"

# Creating object
dog = Dog()
print(dog.breathe())   # Inherited from LivingBeing
print(dog.eat())       # Inherited from LivingBeing
print(dog.walk())      # Inherited from Animal
print(dog.bark())      # Own method
```

#### Example 3: Multiple Inheritance

```python
# Parent Class 1
class CanFly:
    def fly(self):
        return "Flying in the sky..."

# Parent Class 2
class CanSwim:
    def swim(self):
        return "Swimming in water..."

# Child Class inherits from both
class Duck(CanFly, CanSwim):
    def quack(self):
        return "Quack! Quack!"

duck = Duck()
print(duck.fly())      # From CanFly
print(duck.swim())     # From CanSwim
print(duck.quack())    # Own method
```

---

### 3. ENCAPSULATION - Data Hiding

Encapsulation protects data by restricting access to it.

```python
class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.__balance = initial_balance  # Private attribute (__)
        self.__pin = "1234"               # Private attribute
    
    # Public method - getter
    def get_balance(self):
        return f"Balance: ${self.__balance}"
    
    # Public method - deposit
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        else:
            return "Amount must be positive"
    
    # Public method - withdrawal
    def withdraw(self, amount, pin):
        if pin != self.__pin:
            return "❌ Invalid PIN!"
        
        if amount > self.__balance:
            return "❌ Insufficient balance!"
        
        if amount > 0:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        else:
            return "Amount must be positive"
    
    # Public method - change PIN
    def change_pin(self, old_pin, new_pin):
        if old_pin != self.__pin:
            return "❌ Old PIN is incorrect!"
        
        self.__pin = new_pin
        return "✅ PIN changed successfully"

# Creating account
account = BankAccount("Ali Khan", 1000)

print(account.account_holder)  # Can access public attribute
print(account.get_balance())   # ✅ Access via method

print(account.deposit(500))    # ✅ Works
print(account.withdraw(200, "1234"))  # ✅ Works with correct PIN
print(account.withdraw(200, "5678"))  # ❌ Fails with wrong PIN

# This will raise AttributeError - cannot access private data directly
# print(account.__balance)  # ❌ Error!
# print(account.__pin)      # ❌ Error!

# But Python allows name mangling (not recommended)
print(account._BankAccount__balance)  # Not recommended, but possible
```

---

### 4. ABSTRACTION - Interface & Implementation

Abstraction hides complex implementation details and shows only necessary features.

```python
from abc import ABC, abstractmethod

# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate area - must be implemented by child classes"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate perimeter - must be implemented by child classes"""
        pass
    
    # Concrete method (not abstract)
    def display_info(self):
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")

# Concrete Class 1
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

# Concrete Class 2
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

# Creating objects
rect = Rectangle(5, 4)
circle = Circle(3)

print("Rectangle:")
rect.display_info()
print("\nCircle:")
circle.display_info()

# This would raise an error - cannot instantiate abstract class
# shape = Shape()  # ❌ TypeError!
```

---

## 🎯 REAL-WORLD EXAMPLE: E-Commerce System

Complete system using all OOP concepts:

```python
from abc import ABC, abstractmethod

# 1. ABSTRACTION - Abstract Base Class
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# 2. INHERITANCE - Concrete Payment Methods
class CreditCard(PaymentMethod):
    def __init__(self, card_number, cvv):
        self.__card_number = card_number
        self.__cvv = cvv
    
    def process_payment(self, amount):
        return f"Processing ${amount} via Credit Card"

class UPI(PaymentMethod):
    def __init__(self, upi_id):
        self.upi_id = upi_id
    
    def process_payment(self, amount):
        return f"Processing ${amount} via UPI: {self.upi_id}"

class WalletPayment(PaymentMethod):
    def __init__(self, wallet_name):
        self.__wallet_name = wallet_name
        self.__balance = 5000
    
    def process_payment(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            return f"Processing ${amount} via {self.__wallet_name}. Remaining: ${self.__balance}"
        else:
            return f"Insufficient balance in {self.__wallet_name}"

# 3. POLYMORPHISM - Same method, different implementations
class Order:
    def __init__(self, order_id, amount):
        self.order_id = order_id
        self.amount = amount
    
    def pay(self, payment_method):
        # Works with ANY payment method that has process_payment()
        result = payment_method.process_payment(self.amount)
        return result

# ENCAPSULATION - Private data
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.__email = email  # Private
        self.__orders = []    # Private
    
    def get_email(self):
        return self.__email
    
    def add_order(self, order):
        self.__orders.append(order)
    
    def get_order_count(self):
        return len(self.__orders)

# Using the system
print("=== E-Commerce Payment System ===\n")

# Create customer
customer = Customer("Rajesh Kumar", "rajesh@email.com")

# Create payment methods
credit_card = CreditCard("1234-5678-9012-3456", "123")
upi = UPI("rajesh@okhdfcbank")
wallet = WalletPayment("PhonePe")

# Create orders
order1 = Order("ORD001", 500)
order2 = Order("ORD002", 1200)
order3 = Order("ORD003", 800)

# Process payments with polymorphism
print(f"Order 1: {order1.pay(credit_card)}")
print(f"Order 2: {order2.pay(upi)}")
print(f"Order 3: {order3.pay(wallet)}")

customer.add_order(order1)
customer.add_order(order2)
customer.add_order(order3)

print(f"\nTotal orders placed: {customer.get_order_count()}")
```

---

## 📋 QUICK COMPARISON TABLE

| Concept | Purpose | Example |
|---------|---------|---------|
| **Polymorphism** | Same interface, different behavior | Dog.speak() vs Cat.speak() |
| **Inheritance** | Reuse code, create hierarchy | Car inherits from Vehicle |
| **Encapsulation** | Protect data, restrict access | Private __password attribute |
| **Abstraction** | Hide complexity, show interface | Abstract Shape class |

---

## ✅ KEY TAKEAWAYS

1. **Polymorphism**: Write generic code that works with multiple types
2. **Inheritance**: Avoid code duplication, create logical hierarchy
3. **Encapsulation**: Protect data with private attributes and methods
4. **Abstraction**: Show only what's needed, hide implementation details

---

## 🎓 Practice Exercises

1. Create a Library Management System with Books, Members, and Transactions
2. Build a Gaming System with different character types (Warrior, Mage, Archer)
3. Design an Employee Management System with different roles (Manager, Developer, Designer)
4. Create a Transportation System (Cars, Bikes, Buses, Trains)
5. Build a Restaurant Menu System with different food categories

---

## 📚 REFERENCES

- GeeksforGeeks - Python OOP Concepts
- Real Python - Object-Oriented Programming in Python
- W3Schools - Python OOP Tutorial
- Python Official Documentation - abc module for Abstraction

---
