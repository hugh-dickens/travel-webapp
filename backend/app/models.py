# app/models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Trip(db.Model):
    __tablename__ = 'trips'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    activity_type = db.Column(db.String(50), nullable=False)
    destination = db.Column(db.String(100), nullable=False)  # Add this line
    cost = db.Column(db.Float)
    carbonFootprint = db.Column(db.String(50))
    duration = db.Column(db.Integer)
    travelMode = db.Column(db.String(50))

    def __repr__(self):
        return f"<Trip {self.name} ({self.activity_type})>"

# Sample data insertion (optional: to be run in your script or shell)
sample_trips = [
    {"name": "Rock climbing in Kalymnos", "activity_type": "rock climb", "destination": "Kalymnos", "cost": 1000/7, "carbonFootprint": "low", "duration": 7, "travelMode": "car"},
    {"name": "Alpine climbing in Ailefroide", "activity_type": "alpine climb", "destination": "Ailefroide", "cost": 2000/10, "carbonFootprint": "medium", "duration": 10, "travelMode": "train"},
    {"name": "Mountain biking in Dolomites", "activity_type": "mountain bike", "destination": "Dolomites", "cost": 1500/5, "carbonFootprint": "low", "duration": 5, "travelMode": "plane"},
    {"name": "Hiking in Aosta Valley", "activity_type": "hike", "destination": "Aosta Valley", "cost": 500/3, "carbonFootprint": "extremely low", "duration": 3, "travelMode": "train"},
]

def add_sample_trips():
    for trip in sample_trips:
        new_trip = Trip(
            name=trip["name"],
            activity_type=trip["activity_type"],
            destination=trip["destination"],
            cost=trip["cost"],
            carbonFootprint=trip["carbonFootprint"],
            duration=trip["duration"],
            travelMode=trip["travelMode"]
        )
        db.session.add(new_trip)
    db.session.commit()
    print("Sample trips added successfully!")

# Call add_sample_trips() to populate the database when needed (for example in a script or shell)
