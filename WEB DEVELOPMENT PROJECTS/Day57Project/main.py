from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    blog_data = response.json()

    return render_template('index.html', blog_data=blog_data)

@app.route('/post/<id>')
def get_blog(id):
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    blog_data = response.json()[int(id) - 1]

    return render_template('post.html', blog_data=blog_data)



if __name__ == "__main__":
    app.run(debug=True)
