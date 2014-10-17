from flask import Flask, render_template, request, session

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


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['passwd']

    if username == 'foo' and password == 'bar':

        session['is_logged_in'] = 'Yes'

        return render_template('index.html', is_logged_in=True)
    else:

        session['is_logged_in'] = 'No'

        return render_template('index.html', is_logged_in=False)


@app.route("/hello")
def hello():
    return render_template('hello.html')


@app.route("/style.css")
def style():
    return render_template('style.css')


if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
