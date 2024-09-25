from flask import Flask, render_template, flash, redirect, url_for
from flask_bootstrap import Bootstrap4
from forms import LoginForm  # Import the form


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
bootstrap = Bootstrap4(app)


app.config['SECRET_KEY'] = 'mysecretkey'  # Required for CSRF protection

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # You can add logic here to authenticate the user
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=form)

@app.route('/denied')
def denied():
    return render_template('denied.html')


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)