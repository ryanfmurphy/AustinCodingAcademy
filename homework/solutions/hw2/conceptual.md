Python course - Assignment 2 SOLUTIONS
======================================

### Problem 1

1. A video game loading a saved state
2. Spreadsheet software reading a CSV file
3. A PDF viewer parsing the contents of a PDF file

### Problem 2

Relative. In relation to `HarmVille.exe`, the path to assets is always just
`assets/`. Since the game files could potentially be installed anywhere on the
file system, it would be impossible to guarantee the absolute path of the assets
directory.

### Problem 3

1. Open the file in read mode and store all of its contents in a string variable
2. Concatenate the string you wish to add to the end of the file to the string
   variable created in part 1.
3. Open the file in write mode, and write the concatenated strings created in
   part 2.

A potential issue with this strategy is that the entire contents of the file
must be stored in memory. Extremely large files may cause the system to expend
its memory resources.

### Problem 4

Suppose Program A and Program B wish to append to the file using the
concatenation strategy described in problem 3. If Program A reads from the file
and concatenates, and then Program B reads from the file before Program A has
had a chance to rewrite the file, Program B's file write will lack the
concatenated string from Program A.

### Problem 5

A comma in the description can throw off naive CSV parsers. Escaping the comma
could be one strategy. The actual strategy implemented in CSV exporters is to
wrap entries containing commas in double quotes.

### Problem 6

1. element - An item in a list
2. index - An item's position in a list, starting at 0.
3. iterate - To go through a list until the end, usually one element at a time.
4. append - To add an element to the end of the list

### Problem 7

A set can represent a collection of valid promocodes for a product at checkout.
A set would be preferred over a list in this case since we mainly want to see if
a promocode entered by the user is in the collection of valid promocodes.

A list can represent the amount of rainfall for each day of the month. Since
sets have no concept of order, you could not easily associate a day of the month
with a data point, whereas lists can use indexes.

### Problem 8

1. Names that describe exactly what the function aims to accomplish - not more,
   not less.
2. Consistent return values types. For example, a function shouldn't return a
   list in one condition and return an integer in another.
3. Not so small that the function is trivial, but not too large where the
   function becomes hard to follow.

### Problem 9

```python
import urllib2

def save_webpage(url,download_path):
    '''
    This function attempts to download the web page at the url specified
    in the `x` argument. The function saves the web page to the file path
    specified by the `y` argument.
    '''
    html = urllib2.urlopen(x).read()
    with open(download_path, 'w') as f:
        f.write(html)

url = raw_input("Enter the web page you would like to download: ")
download_path = raw_input("Enter the file path where the web page should be saved: ")
save_webpage(url, download_path)
```

### Problem 10

```python

air_conditioner = {
    'manufacturer': 'GE',
    'year': 2005,
    'model_number': 'A11011',
    'last_serviced_by': 'John Waters'
}

shopping_cart = {
    'products': [
        'The C Programming Language',
        'Toilet paper',
        'TopoChico'
    ],
    'subtotal': 60.85,
    'payment_method': 'paypal',
    'customer_logged_in': True
}

computer = {
    'ram': '8GB DDR3 1600',
    'serial': '00101ABCB01011',
    'operating_system': 'Windows 8.1',
    'warranty_expired': True
}
```

### Problem 11

A dictionary should be used when you want to refer to the attributes of
something. A list should be use when you need to store many similar items.
