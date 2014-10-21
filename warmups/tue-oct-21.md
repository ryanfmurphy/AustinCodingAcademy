Tuesday Oct 21 - Creating classes in Flask
------------------------------------------

> Today we will be creating a simple flask app that has three pages.

- Create a home page with a welcome message that reads ```Welcome to ACAShop```
- Create a route that can be accessed at ```/person```
- Create a route that can be accessed at ```/product```

For the ```/person``` route, we will be creating a simple form that will contain two fields:
- Person Name
- Person Address
- Submit button

For the ```/product``` route, we will be creating three fields:
- Product Name
- Product Category
- Product Price
- Submit button

On the server side, you will be creating two corresponding ```handler``` functions
- ```def save_person():``` will acquire the person form data, save it to session and return it as a string.
- ```def save_product():``` will acquire the product form data, save it to session and return it as a string.

Once you have the data in session, display everything that the user entered on the homepage.

***

#### Form HTML example
```html
<form name="myForm" action="/some_route" method="post">
    Field Label: <input type="text" name="person_age" size="12" />
    <br/><!-- This is how you make a line break in HTML -->
    <input type="submit" value="Click Me" />
</form>
```

#### Initialize flask app
```python
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = 'mon_key'
```

### Form handling primer
 ```python
# This is how you accept POST form values in your method
@app.route('/person', methods=['POST'])

# This is how to get a form value from the request object in flask
person_name = request.form['person_name']

# This is how you can store values in session
session['is_logged_in'] = 'Yes'

 ```