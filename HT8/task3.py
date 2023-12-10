class Products:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Added product: {product.name}")

    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"\nProduct: {product_name} removed")
                return
        print(f"Product{product_name} is not find")

    def find_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product
        return None


shop = Shop()
item_product_1 = Products("Apple", 1.5)
item_product_2 = Products("Banan", 0.5)
shop.add_product(item_product_1)
shop.add_product(item_product_2)

find_products = shop.find_product("Apple")
if find_products:
    print(f"Product {find_products.name}, price: {find_products.price}")
else:
    print(f"Not found{find_products.name}")

shop.remove_product("Banan")

find_products = shop.find_product("Banan")
if find_products:
    print(f"Product {find_products.name}, price: {find_products.price}")
else:
    print("\nNot found Product")
