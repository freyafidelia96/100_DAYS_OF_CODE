from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm


class Form(FlaskForm):
    rating = FloatField("Your Rating Out of 10 e.g 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired(), Length(max=250)])
    submit = SubmitField('Done')
