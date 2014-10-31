from flask import Flask, render_template, request, session
from tue_oct_14_order_person_product_classes import Person, Product, Order

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = 'mon_key'

@app.route("/")
def index():
    return render_template('index.html', sess=session)


@app.route("/style.css")
def style():
    return render_template('style.css')


@app.route("/person", methods=['POST'])
def person():
    person_name = request.form['name']
    person_address = request.form['address']

    my_person = { 'name' : person_name, 'addy' : person_address }

    person_dict = []

    person_dict.append(my_person)

    session['person_dict'] = my_person

    session['name'] = person_name
    session['address'] = person_address

    return person_name + '' + person_address



@app.route("/product", methods=['POST'])
def product():
    product_name = request.form['product_name']
    product_cat = request.form['product_cat']
    product_price = request.form['product_price']

    my_product = {'product_name': product_name, 'product_cat': product_cat, 'product_price': product_price}

    product_list = []

    try:
        session['product_list'].append(my_product)
    except:
        session['product_list'] = []
        session['product_list'].append(my_product)

    session['product_name'] = product_name
    session['product_cat'] = product_cat
    session['product_price'] = product_price

    return product_name + ' ' + product_cat + ' ' + product_price

@app.route("/order", methods=['POST', 'GET'])
def order():
    products = session['product_list']
    person = Person(session['name'], session['address'])

    product_list = []

    for product in products:
        my_product = Product()
        product_list.append(my_product)

    new_order = Order(person, product_list)
    return new_order.place_order()





if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

