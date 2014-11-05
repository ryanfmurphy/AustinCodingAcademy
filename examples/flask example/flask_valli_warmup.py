__author__ = 'vallivallamsetla'

from flask import Flask, render_template, request, session
from order_person_product_classes import Person, Product, Order

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = 'mon_key'

@app.route('/', methods=['GET'])
def home():
    return render_template("home.html", sess=session)



@app.route('/person', methods=['GET'])
def person():
    return render_template("person.html")


@app.route('/product', methods=['GET'])
def product():
    return render_template("product.html")

@app.route('/save_person', methods=['POST'])
def save_person():
    try:
        session['person']
    except:
        session['person'] = []
    session['person'].append({'name':request.form['person_name'], 'age':request.form['person_age'],'address': request.form['person_address']})


    # person_name = request.form['person_name']
    # person_address = request.form['person_address']

    #return 'My session person: %s, My Person Address:vagra %s' % (session['person_name'], session['person_address'])
    return str(session['person'])



@app.route('/save_product', methods=['POST'])
def save_product():
    try:
        session['products'].append({'name':request.form['product_name'],'category':request.form['product_category'],'price':request.form['product_price']})
    except:
        session['products'] = []
        session['products'].append({'name':request.form['product_name'],'category':request.form['product_category'],'price':request.form['product_price']})
    return str(session['products'])


@app.route('/order')
def place_order():

    # return session['person'][0]['name']

    myPerson = Person(session['person'][0]['name'], session['person'][0]['age'],session['person'][0]['address'])

    myListOfProducts = []

    for product in session['products']:
        newProduct = Product(product['name'], product['category'], product['price'])
        myListOfProducts.append(newProduct)

    myOrder = Order(myPerson, myListOfProducts)
    return myOrder.place_order()



if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
