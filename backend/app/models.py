"""
Database models for trips and saved trips.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Trip(db.Model):
    """
    Represents an available trip in the system
    """
    __tablename__ = "trips"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    activity_type = db.Column(db.String(50), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    cost = db.Column(db.Float)
    carbonFootprint = db.Column(db.String(50))
    duration = db.Column(db.Integer)
    travelMode = db.Column(db.String(50))

    def __repr__(self):
        return f"<Trip {self.name} ({self.activity_type})>"

    def to_dict(self) -> dict:
        """
        Convert trip to dictionary format (useful for JSON responses).
        
        Returns:
            dict: A dictionary representation of the trip
        """
        return {
            "id": self.id,
            "name": self.name,
            "activity": self.activity_type,
            "destination": self.destination,
            "carbonFootprint": self.carbonFootprint,
            "duration": self.duration,
            "travelMode": self.travelMode,
        }

class SavedTrip(db.Model):
    """
    Represents a trip that has been saved by the user.
    """
    __tablename__ = "saved_trips"

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey("trips.id"), nullable=False)
    trip = db.relationship("Trip", backref="saved_trips")

    def __repr__(self):
        return f"<SavedTrip Trip {self.trip_id}>"

    def to_dict(self) -> dict:
        """
        Convert trip to dictionary format (useful for JSON responses).
        
        Returns:
            dict: A dictionary representation of the trip
        """
        return {
            "id": self.id,
            "trip": self.trip.to_dict(),
        }


def add_sample_trips() -> None:
    """
    Adds predefined sample trips to the database if they don't already exist. This is used for initialisation of the database.
    """
    sample_trips = [
        {
            "name": "Rock climbing in Kalymnos",
            "activity_type": "rock climb",
            "destination": "Kalymnos",
            "cost": 1000,
            "carbonFootprint": "low",
            "duration": 7,
            "travelMode": "car",
        },
        {
            "name": "Alpine climbing in Ailefroide",
            "activity_type": "alpine climb",
            "destination": "Ailefroide",
            "cost": 2000,
            "carbonFootprint": "medium",
            "duration": 10,
            "travelMode": "train",
        },
        {
            "name": "Mountain biking in Dolomites",
            "activity_type": "mountain bike",
            "destination": "Dolomites",
            "cost": 1500,
            "carbonFootprint": "low",
            "duration": 5,
            "travelMode": "plane",
        },
        {
            "name": "Hiking in Aosta Valley",
            "activity_type": "hike",
            "destination": "Aosta Valley",
            "cost": 500,
            "carbonFootprint": "extremely low",
            "duration": 3,
            "travelMode": "train",
        },
    ]
    for trip in sample_trips:
        new_trip = Trip(
            name=trip["name"],
            activity_type=trip["activity_type"],
            destination=trip["destination"],
            cost=trip["cost"],
            carbonFootprint=trip["carbonFootprint"],
            duration=trip["duration"],
            travelMode=trip["travelMode"],
        )
        db.session.add(new_trip)
    db.session.commit()
    print("Sample trips added successfully!")
