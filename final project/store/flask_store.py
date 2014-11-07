from flask import Flask, render_template, request, session, Response
import MySQLdb
import MySQLdb.cursors
from pprint import pprint
from classes import Product

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = 'store_mon_key'


@app.route('/')
def home_page():
    prod = Product()
    all_products = prod.get_all_products()
    return render_template('index.html', all_products=all_products)


@app.route('/add_cart')
def add_cart():
    """
    Add a product to the user's session
    :return:
    """
    product_id = request.form['product_id']

@app.route("/style.css")
def style():
    return Response(render_template('style.css'), mimetype="text/css")


if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)