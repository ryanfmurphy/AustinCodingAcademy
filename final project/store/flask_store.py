from flask import Flask, render_template, request, session, Response, redirect
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


@app.route('/add_cart', methods=['POST'])
def add_cart():
    """
    Add a product to the user's session
    :return:
    """

    product_id = request.form['product_id']
    quantity = request.form['quantity']


    cart = {'product_id': product_id, 'quantity': quantity}

    try:
        session['product_list']
    except:
        session['product_list'] = []
    session['product_list'].append(cart)


    return redirect('/cart')

@app.route('/cart')
def cart():
    prod = Product()
    for product in session['product_list']:
        product['product'] = prod.get_product_by_id(int(product['product_id']))
    return render_template('cart.html', prod_list = session['product_list'])


@app.route('/delete_cart', methods = ["POST"])
def delete():
    product_list = session['product_list']
    product_id = request.form['product_id']
    for key, product in enumerate(product_list):
        if product_id == product['product_id']:
            del product_list[key]
    session['product_list'] = product_list
    return redirect('/cart')

@app.route('/checkout_total', methods= ["POST", "GET"])
def checkout_total():
    #compute total cost, and show line items
    total = 0
    prod = Product()
    for product in session['product_list']:
        prod_row = prod.get_product_by_id(int(product['product_id']))
        total += float(prod_row['price']) * float(product['quantity'])
    return str(total)

@app.route('/checkout', methods = ["POST", "GET"])
def checkout():
    return render_template('checkout.html', prod_list = session['product_list'], order_total = checkout_total())



@app.route("/style.css")
def style():
    return Response(render_template('style.css'), mimetype="text/css")


if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)