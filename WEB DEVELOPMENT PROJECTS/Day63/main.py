from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

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

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'


class Base(DeclarativeBase):
    pass


# Create the extension
db = SQLAlchemy(model_class=Base)

# Initialise the app with the extension
db.init_app(app)



class Book(db.Model):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f"{self.id} - {self.title} - {self.author} - {self.rating}/10"


# Create the table
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    results = db.session.execute(db.select(Book).order_by(Book.id))
    all_books = results.scalars().all()

    return render_template('index.html', all_books=all_books)


@app.route("/add", methods=['GET','POST'])
def add():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        rating = request.form.get('rating')

        with app.app_context():
            new_book = Book(title=title, author=author, rating=rating)

            db.session.add(new_book)
            db.session.commit()

        return redirect(url_for('home'))

    return render_template('add.html')

@app.route('/editid=<int:id>', methods=['GET','POST'])
def edit(id):
    
    book = db.session.execute(db.select(Book).where(Book.id == id)).scalar()

    if request.method == 'POST':
        rating = request.form.get('new_rating')
    
        book1 = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
        book1.rating = rating

        db.session.commit()

        return redirect(url_for('home'))

    return render_template('edit.html', title=book.title, rating=book.rating)


@app.route('/deleteid=<int:id>')
def delete(id):
    book = db.session.execute(db.select(Book).where(Book.id == id)).scalar()

    db.session.delete(book)
    db.session.commit()

    return redirect(url_for('home'))

    

if __name__ == "__main__":
    app.run(debug=True)

