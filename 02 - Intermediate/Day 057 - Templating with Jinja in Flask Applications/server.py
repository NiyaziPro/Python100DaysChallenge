import requests
from flask import Flask, render_template
from random import randint
from datetime import datetime as dt

app = Flask(__name__)


@app.route("/")
def home():
    random_number = randint(1, 10)
    current_year = dt.now().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<name>")
def guessing(name):
    URL_GENDER = "https://api.genderize.io"
    URL_AGE = "https://api.agify.io"
    params = {"name": name}
    gender = requests.get(url=URL_GENDER, params=params).json()["gender"]
    age = requests.get(url=URL_AGE, params=params).json()["age"]

    return render_template("guess.html", person_name=name, person_gender=gender, person_age=age)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    all_posts = requests.get(blog_url).json()
    return render_template("blog.html",posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
