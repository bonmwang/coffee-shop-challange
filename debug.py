from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order

if __name__ == "__main__":
    c1 = Customer("Alice")
    c2 = Customer("Bob")

    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")

    o1 = Order(c1, coffee1, 4.5)
    o2 = Order(c1, coffee2, 3.0)
    o3 = Order(c2, coffee1, 5.0)

    print(f"{c1.name}'s orders: {len(c1.orders())}")
    print(f"{coffee1.name} average price: {coffee1.average_price}")
    most_aficionado = Customer.most_aficianado(coffee1)
    print(f"Most aficionado for {coffee1.name}: {most_aficionado.name if most_aficionado else 'None'}")