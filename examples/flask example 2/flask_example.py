from flask import Flask, render_template, request, session, Response

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
    return "Name: %s, Address: %s" % (name, address)


@app.route("/product")
def product():
    return render_template('product.html')

@app.route("/style.css")
def style():
    return Response(render_template('style.css'), mimetype="text/css")

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)

