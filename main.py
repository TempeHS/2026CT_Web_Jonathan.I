from flask import Flask
from flask import render_template

app = Flask (__name__)

@app.route('/')
def hello_world():
    back_end_data = "hello"
    return render_template("index.html", front_end_data = back_end_data),200

if __name__ == '__main__':
    app.run(debug=True)