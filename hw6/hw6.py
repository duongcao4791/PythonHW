from statistics import mean


class Product:
    """
    Represent all products sold by the store

    Argument:
    description (string):
    list_price (positive integer): Manufacturer Suggested Retail Price

    Attributes:
    id (integer): ID number of a product
    category (string): denote the category
    serial_number (integer): denote the next available serial number
    stock (integer): number of items in stock
    """

    # stock = 0 #(number of items in stock) is initialized to 0
    stock = 0
    serial_number = 0
    next_serial_number = 1  # next available serial number in that category
    category = 'GN'
    sale_price = 0

    def __init__(self, description, list_price):
        self.description = description
        self.list_price = list_price
        self.serial_number = self.next_serial_number
        self.id = f'{self.category}{self.serial_number:05}'
        self.generate_product_id()
        self.reviews = []
        self.sales = []
        # self._lowest_price = None

    def __str__(self):
        return f'{self.description}\nID:{self.id}\nList price: ${self.list_price:,.2f}' \
               f'\nAvailable in stock: {self.stock}\n'

    @classmethod
    def generate_product_id(cls):
        cls.next_serial_number += 1

    def restock(self, quantity):
        self.stock += quantity

    def review(self, stars, text):
        self.stars = stars
        self.text = text
        self.reviews.append(self.text)
        self.reviews.append(self.stars)

    def sell(self, quantity, sale_price):
        if quantity > self.stock:
            print('There are only' + f' {self.stock} ' + 'available')
            self.quantity = self.stock
            self.sale_price = sale_price
        else:
            self.quantity = quantity
            self.sale_price = sale_price

        self.stock -= self.quantity
        for i in range(0, self.quantity):
            self.sales.append(sale_price)

    @property
    def lowest_price(self):
        if not self.sales:
            return
        else:
            return min(self.sales)

    @property
    def average_rating(self):
        return mean(self.reviews[i] for i in self.reviews[1::2])


def main():
    print(">>>Step1:<<<")
    sunglasses = Product("Vans Hip Cat Sunglasses", 14)
    print(Product.category)  # GN
    print(Product.next_serial_number)  # 2
    print(sunglasses.id)  # GN000001
    print(sunglasses.description)  # Vans Hip Cat Sunglasses
    print(sunglasses.list_price)  # 14
    print(sunglasses.stock)  # 0
    print(sunglasses.reviews)  # []
    print(sunglasses.sales)  # []

    headphones = Product("Apple Airpods", 159)
    sunglasses.restock(20)
    headphones.restock(5)

    print(sunglasses)  # Vans Hip Cat Sunglasses
    # Product ID: GN000001
    # List price: $14.00
    # Available in stock: 20

    print(headphones)  # Apple Airpods
    # Product ID: GN000002
    # List price: $159.00
    # Available in stock: 5

    sunglasses.sell(3, 14)
    sunglasses.sell(1, 10)
    print(sunglasses.sales)  # [14, 14, 14, 10]

    headphones.sell(8, 140)  # There are only 5 available
    print(headphones.sales)  # [140, 140, 140, 140, 140]

    print(sunglasses)  # Vans Hip Cat Sunglasses
    # Product ID: GN000001
    # List price: $14.00
    # Available in stock: 16

    print(headphones)  # Apple Airpods
    # Product ID: GN000002
    # List price: $159.00
    # Available in stock: 0

    sunglasses.restock(10)
    print(sunglasses)  # Vans Hip Cat Sunglasses
    # Product ID: GN000001
    # List price: $14.00
    # Available in stock: 26

    headphones.restock(20)
    print(headphones)  # Apple Airpods
    # Product ID: GN000002
    # List price: $159.00
    # Available in stock: 20

    sunglasses.review(5, "Great sunglasses! Love them.")
    sunglasses.review(3, "Glasses look good but they scratch easily")
    headphones.review(4, "Good but expensive")
    print(sunglasses.reviews)  # [('Great sunglasses! Love them.', 5), ('Glasses look good but they scratch easily', 3)]
    print(headphones.reviews)  # [('Good but expensive', 4)]
    print(Product.category)  # GN
    print(Product.next_serial_number)  # 3

    print('>>>>STEP 2:<<<<')
    print(sunglasses.lowest_price)  # 10
    print(sunglasses.reviews)
    # print(sunglasses.average_rating)  # 4.0
    #
    backpack = Product("Nike Explore", 60)
    # print(backpack.average_rating)  # None

    print(backpack.lowest_price)  # None


if __name__ == "__main__":
    main()
