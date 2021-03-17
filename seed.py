from models import db, Pet
from app import app

db.drop_all()
db.create_all()

db.session.add_all([
    Pet(
        name = 'jerry',
        species = 'flying cat',
        image_url = 'https://static.wikia.nocookie.net/fanon/images/9/9b/Flying_cat.jpg/revision/latest?cb=20171120060856',
        notes = 'he do be flying though',
        available = True
    ),
    Pet(
        name = 'Berry',
        species = 'cat',
        image_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQs9fSoqm0D_uSd1MdxKNC-qiEGu8vl0ixQMA&usqp=CAU',
        notes = 'he do not be flying though',
        available = True
    )
])
db.session.commit()