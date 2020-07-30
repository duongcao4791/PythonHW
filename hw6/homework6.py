# ----------------------------------------------------------------------
# Name:    homework6
# Purpose:
#
# Author(s): Haitao Huang, Duong Cao
# ----------------------------------------------------------------------
"""
Implement four Python classes to represent and manipulate items sold by
a fictional online store.

Step1: Implement Product class
Step2: Implement lowest_price and average_rating properties in Product
Step3: Implement VideoGame class
Step4: Implement Book class
Step5: Implement Bundle class
Step6: Add a magic method to the Product class
"""


class Product:
    """
    Represent all products sold by the store
​
    Argument:
    description (string): Product description
    list_price (positive integer): Manufacturer Suggested Retail Price
​
    Attributes:
    id (integer): ID number of a product
    category (string): denote the category
    serial_number (integer): denote the next available serial number
    stock (integer): number of items in stock
    """

    # class variables
    category = 'GN'
    next_serial_number = 1

    def __init__(self, description, list_price):
        self.description = description
        self.list_price = list_price
        self.id = self.generate_product_id()
        self.stock = 0
        self.sales = []
        self.reviews = []

    def __str__(self):
        return f'\n{self.description}\nProduct ID: {self.id}\nList price: $' \
               f'{self.list_price:,.2f}\nAvailable in stock: {self.stock}\n'

    def __add__(self, other):
        """
        Add objects to the Bundle
        :param other: Bundle
        :return: Bundle
        """
        return Bundle(self, other)

    def restock(self, quantity):
        """
        Update the stock attribute
        :param quantity: (integer) new number of items in stocl
        :return: None
        """
        self.stock += quantity

    def review(self, stars, text):
        """
        Add user reviews to reviews list
        :param stars: (integer) the number of stars
        :param text:  (string) the text of the review
        :return: None
        """
        self.reviews.append((text, stars))

    def sell(self, quantity, sale_price):
        """
        Add list of sale prices into sales list
        :param quantity: (integer) number of the product was sold
        :param sale_price: (integer) number of price sold
        :return: None
        """
        num = 0
        if quantity > self.stock:
            num = self.stock
        else:
            num = quantity
        self.stock -= num
        for i in range(0, num):
            self.sales.append(sale_price)

    @classmethod
    def generate_product_id(cls):
        """
        Create the product
        :return: a class method for function
        """
        id = f'{cls.category}{cls.next_serial_number:06}'
        cls.next_serial_number += 1
        return id

    @property
    def lowest_price(self):
        """
        Represents the lowest sale price that the product was sold for
        :return: lowest sold price or None
        """
        if self.sales:
            return min(self.sales)
        else:
            return None

    @property
    def average_rating(self):
        """
        Represents the average star rating for the product
        :return: average rating or None
        """
        if self.reviews:
            return round(sum(r[1] for r in self.reviews) / len(self.reviews), 1)
        else:
            return None


class VideoGame(Product):
    """
    Class of Video Game objects

    Argument:
    description (string): Product description
    list_price (positive integer): Manufacturer Suggested Retail Price
​
    Attributes:
    id (integer): ID number of a product
    category (string): denote the category is 'VG'
    serial_number (integer): denote the next available serial number
    stock (integer): number of items in stock
    """

    # class variables
    category = 'VG'
    next_serial_number = 1


class Book(Product):
    """
    Class of Book objects

    Argument:
    description (string): Product description
    list_price (positive integer): Manufacturer Suggested Retail Price
    author (string): author of the book
    pages (positive integer): number of pages
​
    Attributes:
    id (integer): ID number of a product
    category (string): denote the category is 'BK'
    serial_number (integer): denote the next available serial number
    stock (integer): number of items in stock
    """

    # class variables
    category = 'BK'
    next_serial_number = 1

    def __init__(self, description, author, pages, list_price):
        self.author = author
        self.pages = pages
        super().__init__(description, list_price)

    def __eq__(self, other):
        """
        Compare two books by number of pages (equal)
        :param other: Book
        :return: boolean
        """
        return self.pages == other.pages

    def __ne__(self, other):
        """
        Compare two books by number of pages (not equal)
        :param other: Book
        :return: boolean
        """
        return self.pages != other.pages

    def __lt__(self, other):
        """
        Compare two books by number of pages (less than)
        :param other: Book
        :return: boolean
        """
        return self.pages < other.pages

    def __gt__(self, other):
        """
        Compare two books by number of pages (greater than)
        :param other: Book
        :return: boolean
        """
        return self.pages > other.pages

    def __le__(self, other):
        """
        Compare two books by number of pages (less than or equal)
        :param other: Book
        :return: boolean
        """
        return self.pages <= other.pages

    def __ge__(self, other):
        """
        Compare two books by number of pages (greater than or equal)
        :param other: Book
        :return: boolean
        """
        return self.pages >= other.pages


class Bundle(Product):
    """
    Class of Bundle objects created by specifying 2 or more Products

    Argument:
    description (string): Product in the Bundle description
    list_price (positive integer): Manufacturer Suggested Retail Price
    ​
     Attributes:
    id (integer): ID number of a product
    category (string): denote the category is 'BL'
    serial_number (integer): denote the next available serial number
    stock (integer): number of items in stock
    """

    # class variables
    category = 'BL'
    next_serial_number = 1
    bundle_discount = 20

    def __init__(self, product1, product2, *other_products):
        str = f'{product1.description} & {product2.description}'
        total_price = product1.list_price + product2.list_price
        if other_products:
            str += ' ' + ' '.join([f'& {p.description}' for p in other_products])
            total_price += sum([p.list_price for p in other_products])
        super().__init__(str, total_price * (1 - self.bundle_discount / 100))


def main():
    print('>>>>>>STEP 1<<<<<<')
    sunglasses = Product("Vans Hip Cat Sunglasses", 14)
    print(Product.category)
    print(Product.next_serial_number)
    print(sunglasses.id)
    print(sunglasses.description)
    print(sunglasses.list_price)
    print(sunglasses.stock)
    print(sunglasses.reviews)
    print(sunglasses.sales)
    headphones = Product("Apple Airpods", 159)
    sunglasses.restock(20)
    headphones.restock(5)
    print(sunglasses)
    print(headphones)
    sunglasses.sell(3, 14)
    sunglasses.sell(1, 10)
    print(sunglasses.sales)
    headphones.sell(8, 140)  # There are only 5 available
    print(headphones.sales)
    print(sunglasses)
    print(headphones)
    sunglasses.restock(10)
    print(sunglasses)
    headphones.restock(20)
    print(headphones)
    sunglasses.review(5, "Great sunglasses! Love them.")
    sunglasses.review(3, "Glasses look good but they scratch easily")
    headphones.review(4, "Good but expensive")
    print(sunglasses.reviews)
    print(headphones.reviews)
    print(Product.category)
    print(Product.next_serial_number)

    print('')
    print('>>>>>>STEP 2<<<<<<')
    print(sunglasses.lowest_price)
    print(sunglasses.average_rating)
    backpack = Product("Nike Explore", 60)
    print(backpack.average_rating)
    print(backpack.lowest_price)

    print('')
    print('>>>>>>STEP 3<<<<<<')
    mario = VideoGame('Mario Tennis Aces', 50)
    mario.restock(10)
    mario.sell(3, 40)
    mario.sell(4, 35)
    print(mario)
    print(mario.lowest_price)
    mario.review(5, "Fun Game!")
    mario.review(3, "Too easy")
    mario.review(1, "Boring")
    print(mario.average_rating)
    lego = VideoGame('LEGO The Incredibles', 30)
    print(lego)
    lego.restock(5)
    lego.sell(10, 20)
    print(lego)
    print(lego.lowest_price)
    print(VideoGame.category)
    print(VideoGame.next_serial_number)

    print('')
    print('>>>>>>STEP 4<<<<<<')
    book1 = Book("The Quick Python Book", "Naomi Ceder", 472, 39.99)
    print(book1.author)
    print(book1.pages)
    book1.restock(10)
    book1.sell(3, 30)
    book1.sell(1, 32)
    book1.review(5, "Excellent how to guide")
    print(book1)
    print(book1.average_rating)
    print(book1.lowest_price)
    book2 = Book("Learning Python", "Mark Lutz", 1648, 74.99)
    book1.restock(20)
    book1.sell(2, 50)
    print(book2)
    print(book1 > book2)
    print(book1 < book2)
    print(Book.category)
    print(Book.next_serial_number)

    print('')
    print('>>>>>>STEP 5<<<<<<')
    bundle1 = Bundle(sunglasses, backpack, mario)
    print(bundle1)
    bundle1.restock(3)
    bundle1.sell(1, 90)
    print(bundle1)
    bundle1.sell(2, 95)
    print(bundle1)
    bundle1.restock(3)
    bundle1.sell(1, 90)
    print(bundle1)
    bundle1.sell(3, 95)
    print(bundle1)
    print(bundle1.lowest_price)
    bundle2 = Bundle(book1, book2)
    bundle2.restock(2)
    print(bundle2)
    print(Bundle.category)
    print(Bundle.next_serial_number)
    print(Bundle.bundle_discount)

    print('')
    print('>>>>>>STEP 6<<<<<<')
    back_to_school_bundle = backpack + book1
    print(back_to_school_bundle)
    best_bundle = sunglasses + headphones + book1 + mario
    print(best_bundle)
    # the product id of the best_bundle is BL000006 because we have
    # created a new bundle for each adding ('+')


if __name__ == "__main__":
    main()
