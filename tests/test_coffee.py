import pytest
from coffee_shop.coffee import Coffee
from coffee_shop.customer import Customer
from coffee_shop.order import Order

class TestCoffee:
    def test_name_validation(self):
        with pytest.raises(TypeError):
            Coffee(123)
        with pytest.raises(ValueError):
            Coffee("ab")
        coffee = Coffee("Latte")
        with pytest.raises(AttributeError):
            coffee.name = "Mocha"

    def test_orders(self):
        coffee = Coffee("Espresso")
        c = Customer("Alice")
        o = Order(c, coffee, 3.0)
        assert o in coffee.orders()

    def test_customers(self):
        coffee = Coffee("Cappuccino")
        c1 = Customer("Bob")
        c2 = Customer("Charlie")
        Order(c1, coffee, 4.0)
        Order(c2, coffee, 4.5)
        assert len(coffee.customers()) == 2

    def test_num_orders(self):
        coffee = Coffee("Latte")
        c = Customer("Dave")
        Order(c, coffee, 3.5)
        Order(c, coffee, 4.0)
        assert coffee.num_orders() == 2

    def test_average_price(self):
        coffee = Coffee("Mocha")
        c = Customer("Eve")
        Order(c, coffee, 3.0)
        Order(c, coffee, 5.0)
        assert coffee.average_price() == 4.0