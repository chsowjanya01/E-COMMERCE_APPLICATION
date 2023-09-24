from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample product data
products = [
    {"name": "Product 1", "price": 10.00},
    {"name": "Product 2", "price": 20.00},
    {"name": "Product 3", "price": 30.00},
]

# Cart data
cart = []
cart_total = 0.00

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/add_to_cart/<string:name>/<float:price>')
def add_to_cart(name, price):
    global cart_total
    cart.append({"name": name, "price": price})
    cart_total += price
    return jsonify({"message": "Item added to cart."})

@app.route('/checkout')
def checkout():
    global cart, cart_total
    cart.clear()
    cart_total = 0.00
    return jsonify({"message": "Checkout successful."})

if __name__ == '__main__':
    app.run(debug=True)
