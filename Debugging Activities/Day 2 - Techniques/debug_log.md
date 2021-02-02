# Debug Log

**Explain how you used the the techniques covered (Trace Forward, Trace Backward, Divide & Conquer) to uncover the bugs in each exercise. Be specific!**

In your explanations, you may want to answer:

- What is the expected vs. actual output?
- If there is a stack trace, what usefula information does it contain?
- Which technique did you use, on which line numbers?
- What assumptions did you have about each line of code, and which ones were proven to be wrong?

_Example: I noticed that the program should show pizza orders once a new order is made, and that it wasn't showing any. So, I used the trace forward technique starting on line 13. I discovered the bug on line 27 was caused by a typo of 'pzza' instead of 'pizza'._

_Then I noticed another bug ..._

## Exercise 1

[[Your answer goes here!]]
- I had environment issue but I had to run these 2 commands to get it working

`pip3 install flask`

`pip3 install flask_splalchemy`

- I also forgot how to run app.py. Solution is 

`flask run`

**Fixes on `app.py`**
- In `pizza_order_submit()` method, change the form keys to match the with `home.html`
    - name to order_name
    - size to pizza_size
- Still in `pizza_order_submit()`, use `getlist` of toppings instead of a regular `get`
- Still in `pizza_order_submit()`, commit the database changes after adding the pizza
- Still in `pizza_order_submit()`, change the redirect url to `'home'`
- For `fulfill_order()`, change the route's method from POST to GET request


## Exercise 2

[[Your answer goes here!]]

## Exercise 3

[[Your answer goes here!]]
