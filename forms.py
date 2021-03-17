from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, AnyOf, URL, NumberRange

class PetForm(FlaskForm):
    name = StringField('Pet Name',[InputRequired(message='Pet name is required.')])
    
    species = StringField('Species',[InputRequired(), AnyOf(['cat','dog','porcupine'],message='Species must be cat, dog, or porcupine.')])

    image_url = StringField('Image URL',[Optional(), URL(message='Image Url must be a valid url, if provided.')])

    age = IntegerField('Age in years',[Optional(), NumberRange(min=0,max=30,message='Age must be between 0 and 30, if provided.')])

    notes = TextAreaField('Notes',[Optional()])

    available = BooleanField('Available for adoption', default='checked')

class EditPetForm(FlaskForm):
    image_url = StringField('Image URL',[Optional(), URL(message='Image Url must be a valid url, if provided.')])

    notes = TextAreaField('Notes',[Optional()])

    available = BooleanField('Available for adoption', default='checked')
