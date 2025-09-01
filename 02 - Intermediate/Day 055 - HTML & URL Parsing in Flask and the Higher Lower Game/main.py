from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def wrapper():
        return f"<b>{func()}</b>"

    return wrapper


def make_emphasis(func):
    def wrapper():
        return f"<em>{func()}</em>"

    return wrapper


def make_underlined(func):
    def wrapper():
        return f"<u>{func()}</u>"

    return wrapper


def make_text_align_center(func):
    def wrapper():
        return f'<div style="text-align:center">{func()}</div>'

    return wrapper


@app.route("/")
def hello():
    return ('<h1 style="text-align: center; color:green">Hello, Flask :)</h1>'
            '<p>This is a paragraph.</p>'
            '<img src="https://www.petmagazin.bg/wp-content/uploads/2020/08/Dog_Samoyed_Desktop-1.jpg">'
            '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExb3didHozbXh0aDdyMmo1eG8zaXhrZW1jOGIxMTExdGI0NG5mZHZrZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Yr6Xz1tNwRwqY/giphy.gif">'
            '')


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
@make_text_align_center
def say_bye():
    return "Bye!"


@app.route("/user<path:name>")
def greet(name):
    return f"Hello there {name} :)"


if __name__ == "__main__":
    app.run(debug=True)
