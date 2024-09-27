from flask import Flask, render_template, request
import requests
import datetime as dt
import smtplib


app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get('https://api.npoint.io/47da4a64b9b8981992d8')
    blog_posts = response.json()

    year = dt.datetime.now().year

    return render_template('index.html', blog_posts=blog_posts, year=year)

@app.route('/about')
def about():
    year = dt.datetime.now().year
    return render_template('about.html', year=year)

@app.route('/contact')
def contact():
    year = dt.datetime.now().year
    return render_template('contact.html', year=year)

@app.route('/post/<int:id>')
def post(id):
    response = requests.get('https://api.npoint.io/47da4a64b9b8981992d8')
    post = response.json()[id - 1]
    year = dt.datetime.now().year
    return render_template('post.html', post=post, id=id, year=year)

@app.route('/form-entry', methods=['POST'])
def receive_data():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('number')
    message = request.form.get('message')

    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"

    # Send email using SMTP
    try:
        send_email_to_me(email_message)
        return "Message sent successfully!"
    except Exception as e:
        return f"Failed to send email. Error: {e}"


def send_email_to_me(email_message):
    # Your email credentials (update with your own email)
    sender_email = "freyafidelia@gmail.com"  # Update with your email
    sender_password = "xxofikeukgfnjqay"        # Update with your email password
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
        connection.login(sender_email, sender_password)
        connection.sendmail(sender_email, sender_email, email_message)

if __name__ == '__main__':
    app.run(debug=True)