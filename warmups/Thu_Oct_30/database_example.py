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

select_query = 'SELECT * FROM person order by person_name DESC;'
cur.execute(select_query)
people = cur.fetchall()

for person in people:
    print person['person_name']


# Commit this whole transaction to MySQL atomically. If any one statement fails, everything fails.
conn.commit()