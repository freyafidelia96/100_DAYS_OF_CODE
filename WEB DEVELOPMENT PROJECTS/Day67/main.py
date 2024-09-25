from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL, Length
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime as dt

CURRENT_DATE = dt.now()
'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['CKEDITOR_PKG_TYPE'] = 'standard'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(450), nullable=False)


class BlogPostForm(FlaskForm):
    title = StringField('Blog Post Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField('Author Name', validators=[DataRequired()])
    image_url = StringField('Background Image URL', validators=[DataRequired(), URL(), Length(max=500)])
    body = CKEditorField('Blog Content', validators=[DataRequired()])
    submit = SubmitField('Submit')


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    get_posts =db.session.execute(db.select(BlogPost))
    posts = get_posts.scalars().all()
    return render_template("index.html", all_posts=posts, year=CURRENT_DATE.year)

# TODO: Add a route so that you can click on individual posts.
@app.route('/show_post/<post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    return render_template("post.html", post=requested_post, year=CURRENT_DATE.year)


# TODO: add_new_post() to create a new blog post
@app.route('/new-post', methods=['GET', 'POST'])
def new_post():
    form = BlogPostForm()

    if form.validate_on_submit():
        newPost = BlogPost(
            title = form.title.data,
            subtitle = form.title.data,
            date = CURRENT_DATE.strftime("%B %d, %Y"),
            body = form.body.data,
            img_url = form.image_url.data,
            author = form.author.data
        )
        db.session.add(newPost)
        db.session.commit()

        return redirect(url_for("get_all_posts"))
    
    return render_template('make-post.html', form=form, year=CURRENT_DATE.year)

# TODO: edit_post() to change an existing blog post
@app.route('/edit-post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    print(post_id)
    post_to_be_edited = db.get_or_404(BlogPost, post_id)

    form = BlogPostForm(
        title= post_to_be_edited.title,
        subtitle= post_to_be_edited.subtitle,
        author= post_to_be_edited.author,
        body= post_to_be_edited.body,
        image_url=post_to_be_edited.img_url, 
    )

    if form.validate_on_submit():
        post_to_be_edited.title = form.title.data
        post_to_be_edited.subtitle = form.subtitle.data
        post_to_be_edited.author = form.author.data
        post_to_be_edited.body = form.body.data
        post_to_be_edited.img_url = form.image_url.data
        post_to_be_edited.date = CURRENT_DATE.strftime("%B %d, %Y")

        db.session.commit()
        return redirect(url_for('get_all_posts'))
    
    return render_template('make-post.html', form=form, year=CURRENT_DATE.year)


# TODO: delete_post() to remove a blog post from the database
@app.route('/delete-post/<post_id>')
def delete_post(post_id):
    post_to_be_deleted = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_be_deleted)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")





if __name__ == "__main__":
    app.run(debug=True, port=5003)
