from flask import Flask, render_template, request, session
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
    session['product_name'] = product_name
    session['product_cat'] = product_cat
    session['product_price'] = product_price
    return product_name + ' ' + product_cat + ' ' + product_price


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
