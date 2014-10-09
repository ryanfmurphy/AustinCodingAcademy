Warm-up Thu Oct 9: File Format <=> Dict
=======================================

Suppose you are building an e-commerce system, and you have a file called
"orders.txt" that contains information about your customers' orders.

The "orders.txt" file has a format that looks like this:

    Customer Name
    Item Purchased
    Cost in dollars (with no $)
    Customer Name
    Item Purchased
    Cost in dollars (with no $)
    Customer Name
    Item Purchased
    Cost in dollars (with no $)
    ...

So for example:

    Joe Smith
    Organic Chocolate Bar
    5.0
    Jill Meyer
    "Chemistry for Smart People" Textbook
    20.0
    Ashley Grundle
    Beginner's Lego Kit
    10.0

## Pair up and each pair choose 1 of the 2 options: 

### 1) Reader/Parser

Write a function that reads the file "orders.txt" and puts the data in a list
of dictionaries, each dictionary having the keys "name","product" and "cost".
The output if you fed in the above example would look like this:

    [
        { 'name': 'Joe Smith' 'product': 'Organic Chocolate Bar' 'cost': 5.0 },
        { 'name': 'Jill Meyer', 'product': 'Chemistry for Smart People', 'cost': 20.0 },
        { 'name': Ashley 'Grundle', 'product': 'Beginner's Lego Kit', 'cost': 10.0 }
    ]

### 2) Writer/Saver

Write a function that takes a list of dictionaries like the above, and writes
it into a the file "orders.txt" in the format shown, with name, product, and
cost all each on their own line.

### Extra Credit

You get extra credit if your functions are written in a way where it would be easy to add more fields to the file format.

