from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/personal_site')
def personal_site():
    return render_template('index1.html')


if __name__ == "__main__":
    app.run(debug=True)