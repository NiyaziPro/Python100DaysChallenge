from flask import Flask, render_template
from random import randint
from datetime import datetime as dt

app = Flask(__name__)

@app.route("/")
def home():
    random_number = randint(1,10)
    current_year = dt.now().year
    return render_template("index.html", num=random_number,year=current_year)


if __name__ == "__main__":
    app.run(debug=True)