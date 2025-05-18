# ☕ Coffee Shop Challenge

A Python implementation modeling a coffee shop's ordering system with three core models: `Coffee`, `Customer`, and `Order`, demonstrating object-oriented programming principles and many-to-many relationships.

## Table of Contents
- [Project Structure](#project-structure)
- [Models Overview](#models-overview)
- [Installation](#installation)
- [Usage Examples](#usage-examples)
- [Testing](#testing)
- [Data Relationships](#data-relationships)
- [Validation Rules](#validation-rules)
- [Bonus Features](#bonus-features)

## Project Structure
coffee-shop-challenge/
├── Pipfile # Python dependencies
├── debug.py # Manual testing script
├── customer.py # Customer model implementation
├── coffee.py # Coffee model implementation
├── order.py # Order model implementation
└── tests/
├── customer_test.py # Customer model tests
├── coffee_test.py # Coffee model tests
└── order_test.py # Order model tests


## Models Overview

### Customer Model
- **Properties**:
  - `name`: Enforced as string (1-15 characters)
- **Key Methods**:
  - `orders()`: Returns all orders placed by this customer
  - `coffees()`: Returns unique coffees ordered by this customer
  - `create_order(coffee, price)`: Creates and returns a new order
- **Class Method**:
  - `most_aficionado(coffee)`: Identifies top spender for a specific coffee

### Coffee Model
- **Properties**:
  - `name`: Immutable string (minimum 3 characters)
- **Key Methods**:
  - `orders()`: Returns all orders for this coffee
  - `customers()`: Returns unique customers who ordered this coffee
  - `num_orders()`: Counts total orders for this coffee
  - `average_price()`: Calculates mean order price

### Order Model
- **Properties**:
  - `customer`: Linked Customer instance (type-checked)
  - `coffee`: Linked Coffee instance (type-checked)
  - `price`: Immutable float (1.0-10.0 range)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/<your-username>/coffee-shop-challenge.git
cd coffee-shop-challenge
Set up the virtual environment:

bash
pipenv install
pipenv shell
Usage Examples
Basic Setup
python
from customer import Customer
from coffee import Coffee
from order import Order

# Create instances
alice = Customer("Alice")
latte = Coffee("Latte")

# Create orders
order1 = Order(alice, latte, 4.5)
order2 = alice.create_order(latte, 3.8)
Querying Relationships
python
# Get all orders for a customer
print(alice.orders())  # [order1, order2]

# Get unique coffees ordered by a customer
print(alice.coffees())  # [latte]

# Get average price of a coffee
print(latte.average_price())  # 4.15
Bonus Feature
python
# Find top spender for a coffee
top_customer = Customer.most_aficionado(latte)
print(f"Top spender: {top_customer.name}")
Testing
Run all tests:

bash
python -m pytest tests/
Or run specific test files:

bash
python -m pytest tests/customer_test.py
Data Relationships
Diagram
Code

Validation  Rules
Model	      Property  Validation Rules
Customer	  name	    String,     1-15 chars
Coffee	    name	    String,     ≥3 chars, immutable
Order	      price	    Float,      1.0-10.0, immutable
Order	      customer	Must be Customer instance
Order	      coffee	  Must be Coffee instance
Bonus       Features

The project includes an advanced class method:

python
Customer.most_aficionado(coffee)
This identifies which customer has spent the most money on a particular coffee variety, returning None if there are no orders.

Design Principles
Single Source of Truth: All relationships are maintained through the Order model

Immutability: Critical properties like coffee names and order prices cannot be modified after creation

Type Safety: All properties are strictly type-checked

Data Integrity: Validation rules enforce business requirements


This README provides:
- Clear installation instructions
- Comprehensive usage examples
- Visual relationship diagrams
- Detailed validation rules
- Testing guidance
- Explanation of design principles
- Bonus feature documentation

The formatting uses GitHub-Flavored Markdown with:
- Code blocks for commands and examples
- Tables for validation rules
- Mermaid diagram for relationships
- Clear section organization
- Emphasis on key concepts

You can customize the GitHub URL and add any additional project-specific notes as needed. The README serves as complete documentation for both users and developers of the project.