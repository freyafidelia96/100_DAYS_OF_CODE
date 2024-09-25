from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


# Initialize Flask app and set up database
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
        return f"<Book(title='{self.title}', author='{self.author}', rating={self.rating})>"
    

# Create the table
with app.app_context():
    db.create_all()


# with app.app_context():
#     new_book = Book(id=1, title='Harry Potter', author='J. K. Rowling', rating=9.3)

#     db.session.add(new_book)

#     db.session.commit()


with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars().all()

with app.app_context():
    book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()

# with app.app_context():
#     book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
#     book_to_update.title = "Harry Potter and the Chamber of Secrets"
#     db.session.commit()


book_id = 1
# with app.app_context():
#     # book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#     book_to_update = db.get_or_404(Book, book_id)  
#     book_to_update.title = "Harry Potter and the Goblet of Fire"
#     db.session.commit()  


with app.app_context():
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()