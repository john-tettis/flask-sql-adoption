from flask_sqlalchemy import  SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):

    id = db.Column(
        db.Integer,
        primary_key = True,
        auto_increment = True
    )
    name = db.Column(
        db.String(45),
        nullable = False
    )
    species = db.Column(
        db.String,
        nullable = False
    )
    image_url = db.Column(
        db.Text,
        nullable = True
    )
    age = db.Column(
        db.Integer,
        nullable =True
    )
    notes = db.Column(
        db.Text,
        nullable = True
    )
    available = db.Column(
        db.Boolean,
        nullable = False,
        default = True
    )