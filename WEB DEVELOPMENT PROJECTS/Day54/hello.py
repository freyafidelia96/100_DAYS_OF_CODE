from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        text = function()
        return f'<b>{text}</b>'
    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        text = function()
        return f'<em>{text}</em>'
    return wrapper_function


def make_underline(function):
    def wrapper_function():
        text = function()
        return f'<u>{text}</u>'
    return wrapper_function


@app.route('/')
@make_bold
@make_emphasis
@make_underline
def hello():
    return "Hello, World!"


@app.route('/username/<name>')
def say_hello(name):
    return f'Hello! {name}'


if __name__ == "__main__":
    app.run(debug=True)