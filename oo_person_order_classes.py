"""
#note - This class is #deprecated as of Tue Oct 14 2014
For a more up-to-date Person / Product / Order interface, see order_person_product_classes.py
"""

class Person:
    def __init__(self, name, bank_balance):
        self.name = name
        self.balance = bank_balance

    def can_afford(self, order_total):
        """
        Can this person afford the order?
        :param float order_total: What is the person's order total?
        :return: boolo sorr
        """
        if self.balance > order_total:
            return True
        else:
            return False


class Order:
    def __init__(self, person, items):
        """
        Order for hamazon
        :param Person person: Who placed the order
        :param list(dict) items: These are items in your cart
        :return: None
        """
        self.person = person
        self.cart_items = items

    def get_order_total(self):
        """
        This method gets our order total
        :return: float
        """
        order_total = 0
        for item in self.cart_items:
            order_total += item['price']
        return order_total

    def place_order(self):
        """
        Place the order, charge the card, write to the DB, send an email....
        :return: None
        """

        order_total = self.get_order_total()

        if self.person.can_afford(order_total):
            print 'This person is stinkin rich!'
        else:
            print "No soup for you!"
    


if __name__ == "__main__":
    items = [
        {'item_id': 234, 'item_name': 'Keyboard', 'price': 12},
        {'item_id': 564, 'item_name': 'Mouse', 'price': 4.54},
        {'item_id': 876, 'item_name': 'Laptop', 'price': 1200.22}]

    myPerson = Person('Samir', bank_balance=5000.25)
    myOrder = Order(myPerson, items)
    orderTotal = myOrder.get_order_total()
    print "Order Total: %f" % orderTotal
    myOrder.place_order()

