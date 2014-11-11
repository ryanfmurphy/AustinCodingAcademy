Final Class Project: Finishing the E-commerce App
-------------------------------------------------
The final 2 weeks of the class are going to be spent on the Final Project, which is to get our Products/Persons/Orders app to a moderately finished state.  If you already have your app working to the Minimum Requirements listed below, you may work on Extra Features, or, if you wish, take on another small project of your own choosing.

You may use the code in the `store` directory to give you a head-start.


## Minimum Requirements / MVP "Minimum Viable Product" ##
Completion of an E-Commerce App that meets all these requirements will serve as your Final Exam, enabling you to graduate from this class and receive a certification showing that you've learned the basic software development skills needed to create a real-world Web Application.

* Show a catalog of Products that are stored in the database
* Provide a rudimentary Login Form where the User can enter their Name and a Password.  For now you can just blindly trust what the user says - you do not have to keep track of the User's info in the database or check their password for this project.
* Allow the User to select Products and choose a Quantity they would like to purchase.  You can connect to the online MySQL instance Samir gave you the credentials for.  You can either use the catalog of Products already in the `acadb` database, or create your own database with your own Products.  When the User hits Submit, the items are added to his/her Cart (stored in the Session).
* Provide a "Check Out" button that a User can click when they are done adding items to their Cart. When the user Checks Out, display an invoice containing the User's name, each Product purchased, the Quantity, and the Total Cost owed.

## Extra Features ##
You may optionally implement 1 or more of these Extra Features in order to further hone your learning and receive additional certification from the School showing that you've gone above and beyond in your studies.

* email the invoice / receipt when order is placed
* instead of you making up your own products, have a product catalog to choose from
* more robust login system: keep track of users / passwords
  can use person class for users, add a password field
  make pending orders persist in the system: can log out and back in
* payment system: e.g. use Braintree, Stripe or PayPal to allow people to purchase the product
* users can log in and view their order history
* make front-end HTML/CSS nice and stylish, make messaging on site / UI / page flow smooth and intuitive


## Other Extra Credit Option: A separate Python Project of your own Choosing ##

If you choose to do a separate project, then as a first step, please send us a description of the project:

* What are you trying to accomplish?  What is the purpose of the program?
* How specifically is the program supposed to behave?
* What is your initial overall plan of how to create the program?  No need for too many details, just an overall description will do.
* What skills that you've already learned in this class are you applying in order to create the program?
* What skills are you "borderline" on, or needing to learn, in order to complete the program?

