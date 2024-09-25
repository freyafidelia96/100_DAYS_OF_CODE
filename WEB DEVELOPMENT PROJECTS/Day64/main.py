from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from form import Form
import time
from sqlalchemy.exc import OperationalError

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
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Movies.db'

# CREATE DB
class Base(DeclarativeBase):
    pass

# CREATE TABLE
db = SQLAlchemy(model_class=Base)

db.init_app(app)

class Movie(db.Model):
    __tablename__ = 'Movie'

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True)
    year: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String, nullable=True)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String, nullable=True)
    img_url: Mapped[str] = mapped_column(String, nullable=True)


    def __repr__(self):
        return f"Title: {self.title}, Year: {self.year} Description: {self.description} Rating: {self.rating} Ranking: {self.ranking} Review: {self.review} Image URL: {self.img_url} "

class MovieForm(FlaskForm):
    movie_title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add movie')


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    results = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = results.scalars().all()

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", movies=all_movies)




@app.route('/edit<movie_id>', methods=['GET', 'POST'])
def edit(movie_id):
    form = Form()
    movie = db.get_or_404(Movie, movie_id)

    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data

        db.session.commit()
        return redirect(url_for('home'))
    
    movie_title = movie.title
    return render_template('edit.html', movie_title=movie_title, form=form)
    

@app.route('/delete<movie_id>')
def delete(movie_id):
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()

    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    movie_form = MovieForm()

    if movie_form.validate_on_submit():
        api_key = 'e50eb7dacdb693889e903e48cd26263b'

        # Base URL for TMDb API
        base_url = 'https://api.themoviedb.org/3'

        # Search for a movie
        movie_name = movie_form.movie_title.data
        search_url = f'{base_url}/search/movie'

        # Make the request to TMDb API
        response = requests.get(search_url, params={'api_key': api_key, 'query': movie_name})

        # Convert the response to JSON
        data = response.json()
        results = data['results']
        print(f'{results}\n\n\n')

        return render_template('select.html', results=results)
        
    return render_template('add.html', form = movie_form)


@app.route('/update/<movie_title>/<release_date>/<overview>/<image>')
def update_database(movie_title, release_date, overview, image):
    print(image)
    new_movie = Movie(
    title= movie_title,
    year=release_date,
    description=overview,
    rating=0.0,
    ranking=0,
    review='',
    img_url=f"https://image.tmdb.org/t/p/w500/{image}"
    )
    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)
