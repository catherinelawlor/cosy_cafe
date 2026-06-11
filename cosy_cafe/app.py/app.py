from flask import Flask, render_template, request

app = Flask(__name__)

# Menu data structure
menu_items = [
    {"name": "Caramel Latte", "price": "€4.20"},
    {"name": "Iced Vanilla Matcha", "price": "€4.80"},
    {"name": "Chocolate Croissant", "price": "€3.00"},
    {"name": "Strawberry Tart", "price": "€3.50"},
    {"name": "Mocha Iced Coffee", "price": "€4.50"}
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html", items=menu_items)

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    message = None
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        msg = request.form.get("message")
        message = f"Thanks {name}, your message has been received!"
    return render_template("contact.html", message=message)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
