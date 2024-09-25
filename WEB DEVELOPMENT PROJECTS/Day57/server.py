from flask import Flask, render_template
import datetime as dt
import requests

app = Flask(__name__)

# @app.route('/')
# def start():
#     time = dt.datetime.now()

#     current_year = time.year

#     return render_template('index.html', current_year=current_year)

@app.route('/guess/<name>')
def guess(name):
    agify = 'https://api.agify.io'
    genderise = 'https://api.genderize.io'


    parameters = {
        'name':name
    }

    agify_data = requests.get(agify, params=parameters)
    genderise_data = requests.get(genderise, params=parameters)

    age = agify_data.json()['age']
    gender = genderise_data.json()['gender']

    return render_template('index.html', name=name, age=age, gender=gender)

@app.route('/blog')
def blog():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    blog_data = response.json()

    return render_template('blog.html', blog_data=blog_data)


if __name__ == "__main__":
    app.run(debug=True)