from flask import Flask
from flask import render_template

app = Flask (__name__)

@app.route('/index.html')
@app.route('/')
def index():
    card_data = (
        ("KFC", "What is KFC?", "More", "static/images/card1.png", "contact.html"),
        ("Homemade KFC", "How to make chicken", "", "static/images/card2.png"),
        ("KFC Resturaunts", "Description", "Button text", "static/images/card3.png"),
        ("Title", "Description", "Button text", "static/images/card4.png"),
        ("Title", "Description", "Button text", "static/images/card5.png"),
        ("Title", "Description", "Button text", "static/images/card6.png"),
    )
    return render_template("index.html", cards=card_data),200


@app.route('/contact.html')
def contact():
    return render_template("contact.html"), 200

@app.route('/recipes.html')
def recipes():
    return render_template("recipes.html"), 200



if __name__ == '__main__':
    app.run(debug=True)