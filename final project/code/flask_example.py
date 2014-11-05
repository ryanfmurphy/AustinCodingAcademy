from flask import Flask, render_template, request, session, Response
import MySQLdb
import MySQLdb.cursors
from pprint import pprint

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = 'mon_key'


@app.route("/")
def index():
    if session and session['is_logged_in'] == 'Yes':
        is_logged_in = True
    else:
        is_logged_in = False
    return render_template('index.html', is_logged_in=is_logged_in)

@app.route("/person")
def person():
    return render_template('person.html')

@app.route('/save_person',  methods=['POST'])
def save_person():

    name = request.form['name']
    address = request.form['address']

    # Create a connection object by calling the connect() method on MySQLdb
    conn = MySQLdb.connect(host='acadb.cz0wsfs6bppg.us-west-2.rds.amazonaws.com',
    user='root', passwd='something', db='acadb', port=3306,
    cursorclass=MySQLdb.cursors.DictCursor)


    # Acquire a cursor to operate on this connection with MySQL
    cur = conn.cursor()
    select_query = 'insert into person(person_name, person_address) values("%s", "%s")' % (name, address)

    cur.execute(select_query)

    # products = cur.fetchall()
    #
    # # Loop through each returned row and print it to screen nicely
    # for product in products:
    #     pprint(product)

    conn.commit()

    return "<h3 style=\"#c0c0ff;\">Name: %s, Address: %s has been inserted into the database</h3>" % (name, address)


@app.route("/product")
def product():
    return render_template('product.html')

@app.route("/style.css")
def style():
    return Response(render_template('style.css'), mimetype="text/css")

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)

