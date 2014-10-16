from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/hello")
def hello():
    return 'Hello world!'

@app.route("/style.css")
def style():
    return render_template('style.css')

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
