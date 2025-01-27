"""
Setup the main routes for the application
"""

from flask import Blueprint, request, jsonify
from app.calculations.trip import get_trip
from app.models import Trip, db

main = Blueprint("main", __name__)

@main.route("/api/trip-suggestions", methods=["POST"])
def get_trip_suggestions():
    if request.method == "POST":
        preferences = request.json
        trips = get_trip(activity=preferences['activity'], travelMode=preferences['travelMode'], cost=preferences['cost'],
                         carbonFootprint=preferences['carbonFootprint'], duration=preferences['duration'])
        return jsonify([trips])
    else:
        return jsonify({"message": "OPTIONS request received"}), 200  # Respond to OPTIONS requests


# Example usage:
# curl -X POST http://localhost:5000/add_trip \
# -H "Content-Type: application/json" \
# -d '{"name": "Hiking in Aosta Valley", "activity_type": "hike", "destination": "Aosta Valley", "cost": 200, "carbonFootprint": "extremely low", "duration": 3, "travelMode": "train"}'
@main.route('/add_trip', methods=['POST'])
def add_trip():
    data = request.get_json()
    new_trip = Trip(name=data['name'], activity_type=data['activity_type'])
    db.session.add(new_trip)
    db.session.commit()
    return {"message": "Trip added successfully!"}, 201


# curl -X GET http://localhost:5000/api/trips
@main.route('/api/trips', methods=['GET'])
# For debugging purposes: curl http://localhost:5000/api/trips
def get_all_trips():
    trips = Trip.query.all()  # Get all trips from the database
    trips_list = [{"id": trip.id, "name": trip.name, "activity_type": trip.activity_type} for trip in trips]
    return jsonify(trips_list), 200


# curl -X DELETE http://localhost:5000/delete_trip/1
@main.route('/delete_trip/<int:id>', methods=['DELETE'])
def delete_trip(id):
    trip = Trip.query.get_or_404(id)
    db.session.delete(trip)
    db.session.commit()
    return {"message": f"Trip with id {id} deleted successfully!"}, 200
