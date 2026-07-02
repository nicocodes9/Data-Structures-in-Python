# Cash Register Class
class CashRegister:
    def __init__(self, cashier_name):
        self.cashier_name = cashier_name
        self.products = []
        self._item_count = 0

    def add_product(self, product, quantity=1):
        # adding product to a purchase
        for _ in range(quantity):
            self.products.append(product)
        self._item_count += quantity

    def show_product_list(self):
        for product in self.products:
            print(product)

    def remove_product(self, product_name):
        # removing product from a purchase
        for product in self.products:
            if product["name"] == product_name:
                self.products.remove(product)
                self._item_count -= 1
                break

    def update_price(self, product_name, new_price):
        # updating price of a product
        for product in self.products:
            if product["name"] == product_name:
                product["price"] = new_price

    def calculate_subtotal(self):
        subtotal = 0
        for product in self.products:
            subtotal += product["price"]
        return subtotal

    def calculate_taxes(self):
        return self.calculate_subtotal() * 0.05

    def calculate_total(self):
        return self.calculate_subtotal() + self.calculate_taxes()

    def clear(self):
        self.products = []
        self._item_count = 0

# defining products
product1 = {"name": "Pizza", "price": 10.34}
product2 = {"name": "Burger", "price": 5.99}
product3 = {"name": "Soda", "price": 1.50}

# creating a CashRegister instance
register = CashRegister("John Doe")

# adding products
register.add_product(product1, 2)
register.add_product(product2)
register.add_product(product3, 3)

# showing product list
register.show_product_list()

# updating price of a product
register.update_price("Burger", 6.50)

# calculating subtotal
print("Subtotal:", register.calculate_subtotal())

# calculating taxes
print("Taxes:", register.calculate_taxes())

# calculating total
print("Total:", register.calculate_total())

# clearing the purchase
register.clear()
print("Products after clearing:", register.products)
