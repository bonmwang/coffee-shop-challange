import pytest
from coffee_shop.coffee import Coffee
from coffee_shop.customer import Customer
from coffee_shop.order import Order

class TestCustomer:
    def test_name_validation(self):
        with pytest.raises(TypeError):
            Customer(123)
        with pytest.raises(ValueError):
            Customer("")
        with pytest.raises(ValueError):
            Customer("ThisNameIsWayTooLong")

    def test_orders(self):
        c = Customer("Alice")
        coffee = Coffee("Latte")
        o = Order(c, coffee, 4.0)
        assert o in c.orders()

    def test_coffees(self):
        c = Customer("Bob")
        coffee1 = Coffee("Espresso")
        coffee2 = Coffee("Cappuccino")
        Order(c, coffee1, 3.0)
        Order(c, coffee2, 4.0)
        assert len(c.coffees()) == 2

    def test_create_order(self):
        c = Customer("Charlie")
        coffee = Coffee("Mocha")
        o = c.create_order(coffee, 5.0)
        assert o in c.orders()

    def test_most_aficionado(self):
        c1 = Customer("Dave")
        c2 = Customer("Eve")
        coffee = Coffee("Americano")
        Order(c1, coffee, 2.0)
        Order(c1, coffee, 3.0)
        Order(c2, coffee, 4.0)
        assert Customer.most_aficianado(coffee).name == "Dave"