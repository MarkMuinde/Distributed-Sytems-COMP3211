from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError

#form for entering city name that will catch an error if a city is not found
class CityForm(Form):
    city = StringField ('city', validators = [DataRequired(message ='"Invalid city name. Please check spelling, including punctuation marks and capital/small letters"')])
        