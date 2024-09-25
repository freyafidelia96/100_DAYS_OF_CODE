from flask import Flask
import random

number = random.randint(0, 9)

app = Flask(__name__)

@app.route('/')
def home_page():
    return '<h1>Guess a number between 0 and 9</h1>'\
            '<img src="https://i.giphy.com/3o7aCSPqXE5C6T8tBC.webp">'

@app.route('/<int:guess>')
def evalute_guess(guess):
    if guess < number:
        return '<h1 style="color: red">Too low, Try again!</h1><br>'\
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif guess > number:
        return '<h1 style="color: purple">Too High, Try again!</h1><br>'\
                '<img src="https://media1.giphy.com/media/nR4L10XlJcSeQ/200.webp?cid=790b7611i93clq97avfd2jds93giffll3ymlkl6b4nfcu29t&ep=v1_gifs_search&rid=200.webp&ct=g">'
    else:
        return '<h1 style="color: green">You found me!</h1><br>'\
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    

if __name__ == '__main__':
    app.run(debug=True)