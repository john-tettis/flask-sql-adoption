from flask import Flask, render_template,redirect
from models import db, Pet, connect_db
from flask_debugtoolbar import DebugToolbarExtension
from forms import PetForm, EditPetForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY']= 'thisisnotasecret'

app.debug = True
toolbar = DebugToolbarExtension(app)


connect_db(app)
db.create_all()


@app.route('/')
def home_page():
    """Display homepage containing every pet in db"""
    pets = Pet.query.all()
    return render_template('home.html', pets = pets)

@app.route('/add', methods = ['GET','POST'])
def add_new_pet():
    """Display form for a new pet/ handle the submission of said form"""
    form = PetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        image_url = form.image_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        pet = Pet(
            name = name,
            species = species,
            age = age,
            notes = notes,
            available = available,
            image_url=image_url
        )
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add.html', form = form)

@app.route('/<int:id>', methods=['GET','POST'])
def edit_pet(id):
    """Displays an edit pet form, populated by pet with an id of id, or returns 404 on a get request.
    A post request updates the database information and redirects the user to details via get request"""
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.image_url = form.image_url.data
        pet.available = form.available.data
        pet.notes = form.notes.data
        db.session.add(pet)
        db.session.commit()
        return redirect(f'/{id}')
    else:
        return render_template('edit_pet.html', form = form, pet = pet)