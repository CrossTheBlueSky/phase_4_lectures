#Imports
# app from app
# db and Production from models

from models import *
from app import app



# Create application context `with app.app_context():`
# Info on application context: https://flask.palletsprojects.com/en/1.1.x/appcontext/

# Using .query.delete() on the model will let us delete existing data
Pet.query.delete()
# Now we can start populating the data! 
# We can no use the imported db to .add() and .commit()!

scout = Pet(
    name = "Scout",
    species = "Dog",
    color = "Harlequin"
)

db.session.add(scout)
db.session.commit()