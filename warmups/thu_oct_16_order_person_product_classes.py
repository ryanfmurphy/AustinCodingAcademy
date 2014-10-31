"""

Warmup Tue Oct 16 2014
----------------------

We will be taking these classes we've been working on,
and combining them with the functionality that we made
in the 1st Warmup on Thu Oct 9:


Reading From and Writing to the File Format
-------------------------------------------

On Oct 9 we made 2 functions that read from and write to
a file format for the Orders/People/Products:

    https://github.com/ryanfmurphy/AustinCodingAcademy/tree/master/warmups/thu-oct-9-file-format-2-dicts.md


Now we will be taking those functionalities and adding them to this file,
and using them in a way that plays nicely with the classes we've created.

If you have your working solutions from that day, use those!
But if you need to you can use the solutions posted here:

    https://github.com/ryanfmurphy/AustinCodingAcademy/tree/master/warmups/solutions/thu_oct_9_solution.py


1) Import or copy the 2 functions file2dicts() and dicts2file() from
the Oct 9th Warmup into this file.  You may either copy the functions
directly into this file or use an import to gain access to those
functions from within this file.  Create an example file to read the
order data from, and verify that the 2 functions work.


2) Create a function read_order_data_from_file() which uses the
file2dicts() function to read the "orders.txt" file, then takes the
resulting list of dicts and creates any relevant Order(s), Person(s)
and Products(s).

    2a) In your function, create a dictionary called "results" that has
        3 lists in it:

            one called "orders",
            one called "people"
            and one called "products".

        This is where you will build up your result.

    2b) Go through the list of dicts you got from the file2dicts()
        function.

        Every time there is a new Person mentioned, create
        a new Person object and add it to the "people" list.
        If there's already a Person with that name,
        assume it's the same Person and don't make a redundant one.

            (Note: I added a default value of "None" to some of the parameters,
            like age, street_address and bank_balance.  This is so you can
            create Person objects without having to specify these data
            since we have no way of knowing what the age / bank_balance
            would be just by reading the file)

        Every time there is a new Product mentioned, create a new
        Product object with the corresponding Price.  If that product
        name has already been mentioned, no need to create a new
        object.

        Build up 1 Order object for each Person who buys a Product.
        If a Person buys more than one Product (or the same one
        multiple times) then add all their purchases to the same
        Order.

    2c) Return your finished result from the function, so that you and
        others can call the function and get the corresponding data.


3) Use your read_order_data_from_file() function to create all the
proper Objects, and then print out your results.  What Person objects
did you make?  What Products?  What Orders?  And how are they all
connected together?

"""

class Person:
    
    def __init__(self, name, age=None, street_address=None, bank_balance=None):
        """
        Create a new person
        :param string name: Person's full name
        :param int age: Person's age
        :param string street_address: This is their street address
        :return:
        """
        self.person_name = name
        self.age = age
        self.street_address = street_address
        self.bank_balance = bank_balance
        print "Just created a new person! " + self.person_name

    # Getters: very polite
    def get_address(self):  return self.street_address
    def get_name(self):     return self.person_name
    def get_age(self):      return self.age
    
    #done - Add a function / method called can_afford()
    def can_afford(self, order_total):
        if self.bank_balance >= order_total:
            return True
        else:
            return False
    
    def __repr__(self):
        return '<Person "' + self.person_name + '">'

class Product:
    def __init__(self, product_name, product_price, product_category=None):
        self.product_name = product_name
        self.product_category = product_category
        self.product_price = product_price
        self.discount_amount = 0.00

    def set_discount(self, discount_amt): # Setting the discount property
        self.discount_amount = discount_amt

    def get_price(self):
        # This gives us the product price
        # and takes the discount into consideration.
        return self.product_price - self.discount_amount
    
    def __repr__(self):
        return '<Product called "' + self.product_name + '" costing $' + str(self.product_price) + '>'


class Order:
    def __init__(self, ObjPerson, listOfProducts):
        self.ObjPerson = ObjPerson
        self.listOfProducts = listOfProducts

        if len(listOfProducts) == 0:
            raise Exception('Must pass list of Products')

    def place_order(self):
        # Someday this method will place the order, send the email,
        # charge the card etc..etc...
        # But for now just total everything up and print an invoice.
        num_items = 0
        order_total = 0.00
        order_discount = 0.00

        for product in self.listOfProducts:
            order_total = order_total + product.get_price()
            num_items += 1
            order_discount = order_discount + product.discount_amount

        # Print out line items, like an old skool receipt
        for product in self.listOfProducts:
            print "%s\t\t%s\t\t%.2f" % (product.product_name, product.product_category, product.product_price)

        print "\t\t\tDiscount Amount: %.2f" % order_discount
        print "\t\t\tTotal Amount: %.2f" % order_total
    
    #done - Create a function called add_product()
    def add_product(self, new_product):
        self.listOfProducts.append(new_product)
        return self
    
    def __repr__(self): # string representation of an Order object
        return '<Order for ' + self.ObjPerson.person_name + ' consisting of ' + str(self.listOfProducts) + '>'
        

def file2dicts():
    with open('orders.txt') as fh:
        raw_text = fh.read().strip() # strip is important to get rid of the last newline
        lines = raw_text.split('\n')
        names = lines[::3] # every 3rd line
        products = lines[1::3] # every 3rd line starting with the 2nd line
        costs = lines[2::3] # every 3rd line starting with the 3nd line
        results = []
        for i in range(len(names)):
            results.append({'name':names[i], 'product':products[i], 'cost':float(costs[i])})
        return results

from pprint import pprint


"""
2) Create a function read_order_data_from_file() which uses the
file2dicts() function to read the "orders.txt" file, then takes the
resulting list of dicts and creates any relevant Order(s), Person(s)
and Products(s).
"""

def read_order_data_from_file():
    order_info = file2dicts() # a list of things like {'cost': 10000.0, 'name': 'Joe Smith', 'product': 'John Deere Tractor'}
    people_by_name = {}
    products_by_name = {}
    orders_by_person_name = {}
    
    for order_item in order_info:
        
        name = order_item['name']
        if name not in people_by_name: # check if the person already exists
            people_by_name[name] = Person(name)
        person = people_by_name[name]
        
        product_name = order_item['product']
        if product_name not in products_by_name:
            products_by_name[ product_name ] = Product(product_name, order_item['cost'])
        product = products_by_name[ product_name ]
        
        if name in orders_by_person_name:
            # add product to existing order
            orders_by_person_name[name].add_product(product)
        else:
            # create new order
            orders_by_person_name[name] = Order(person, [product])
    
    results = {
        'people': people_by_name.values(),
        'products': products_by_name.values(),
        'orders': orders_by_person_name.values()
    }
    return results

data = read_order_data_from_file()
pprint(data)        

