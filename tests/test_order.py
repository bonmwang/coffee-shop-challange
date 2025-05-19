import pytest
from coffee_shop.coffee import Coffee
from coffee_shop.customer import Customer
from coffee_shop.order import Order

class TestOrder:
    def test_init(self):
        c = Customer("Alice")
        coffee = Coffee("Latte")
        o = Order(c, coffee, 4.0)
        assert o.customer == c
        assert o.coffee == coffee
        assert o.price == 4.0

    def test_price_validation(self):
        c = Customer("Bob")
        coffee = Coffee("Espresso")
        with pytest.raises(TypeError):
            Order(c, coffee, "4.0")
        with pytest.raises(ValueError):
            Order(c, coffee, 0.5)
        o = Order(c, coffee, 5.0)
        with pytest.raises(AttributeError):
            o.price = 6.0

    def test_relationships(self):
        c = Customer("Charlie")
        coffee = Coffee("Cappuccino")
        o = Order(c, coffee, 4.5)
        assert o in c.orders()
        assert o in coffee.orders()
        