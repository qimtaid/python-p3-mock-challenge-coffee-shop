class Coffee:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) <= 2:
            raise ValueError("Name must be a string longer than 2 characters")
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Cannot modify the name")

    def add_order(self, order):
        self._orders.append(order)

    def orders(self):
        return self._orders

    def customers(self):
        return list({order.customer for order in self._orders})

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)


class Customer:
    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters")
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters")
        self._name = value

    def add_order(self, order):
        self._orders.append(order)

    def orders(self):
        return self._orders

    def coffees(self):
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

class Order:
    all = []

    def __init__(self, customer, coffee, price):
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number")
        self.price = price
        self.customer = customer
        self.coffee = coffee
        coffee.add_order(self)
        customer.add_order(self)
        Order.all.append(self)
