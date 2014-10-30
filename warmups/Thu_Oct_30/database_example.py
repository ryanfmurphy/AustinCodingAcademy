# pip install MySQL-python
import MySQLdb
import MySQLdb.cursors
from pprint import pprint

# Create a connection object by calling the connect() method on MySQLdb
conn = MySQLdb.connect(host='acadb.cz0wsfs6bppg.us-west-2.rds.amazonaws.com',
                       user='root', passwd='something', db='acadb', port=3306,
                       cursorclass=MySQLdb.cursors.DictCursor)

# Acquire a cursor to operate on this connection with MySQL
cur = conn.cursor()

select_query = 'SELECT * FROM product'
cur.execute(select_query)
products = cur.fetchall()

# Loop through each returned row and print it to screen nicely
for product in products:
    pprint(product)


# Commit this whole transaction to MySQL atomically. If any one statement fails, everything fails.
conn.commit()