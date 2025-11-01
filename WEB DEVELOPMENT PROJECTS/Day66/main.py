from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def __repr__(self):
        return f"{self.id} {self.name} {self.img_url} {self.map_url} {self.location} {self.seats} {self.has_sockets} {self.has_toilet} {self.has_wifi} {self.can_take_calls} {self.coffee_price}"


    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route('/random', methods=['GET'])
def ranDom():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()

    length_all_cafes = len(all_cafes)

    random_guess = random.randint(1, length_all_cafes)

    random_cafe = db.session.execute(db.select(Cafe).where(Cafe.id == random_guess)).scalar()

    return jsonify(cafe=random_cafe.to_dict())


@app.route('/all', methods=['GET'])
def all():
    all_cafes = db.session.execute(db.select(Cafe)).scalars()

    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route('/search', methods=['GET'])
def search():
    location = request.args.get("loc")
    location_to_search = db.session.execute(db.select(Cafe).where(Cafe.location == location)).scalars().all()

    error = {"Not Found": "Sorry, we don't have a cafe at that location"}

    return jsonify(cafes=[cafe.to_dict() for cafe in location_to_search]) if location_to_search != [] else jsonify(error=error)


# HTTP POST - Create Record
@app.route('/add', methods=["POST"])
def add():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()

    return jsonify(response={"success": "Successfully added the new cafe."})



# HTTP PUT/PATCH - Update Record
@app.route('/update-price/<cafe_id>', methods=["PATCH"])
def update_price(cafe_id):
    try:
        cafe_to_be_updated = db.get_or_404(Cafe, cafe_id)
        cafe_to_be_updated.coffee_price = request.args.get('new_price')
        db.session.commit()
    except Exception:
        return jsonify(error={"Not Found": "Sorry, a cafe with that id was not found in the database"}), 404
    else:
        return jsonify(response={"success": "Successfully added the new cafe."}), 200
    

# HTTP DELETE - Delete Record
@app.route('/report-closed/<cafe_id>', methods=['DELETE'])
def delete(cafe_id):
    inputted_api_key = request.args.get('api-key')
    api_key = 'TopSecretAPIKey'
    if inputted_api_key == api_key:
        try:
            cafe_to_be_deleted = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
            db.session.delete(cafe_to_be_deleted)
            db.session.commit()
        except  Exception as e:
            print(e)
            return jsonify(error={"Not Found": "Sorry, a cafe with that id was not found in the database"}), 404
        else:
            return jsonify(response={"success": "Successfully deleted."}), 200
    else:
        return jsonify({'error':"Sorry, that's is not allowed. Make sure you have the correct api_key."}), 403



if __name__ == '__main__':
    app.run(debug=True)
