"""
Setup the main routes for the application
"""

from flask import Blueprint, request, jsonify
from app.trip_planner import Trip

from app.models import Trip, db, add_sample_trips

main = Blueprint("main", __name__)

@main.route("/api/trip-suggestions", methods=["POST"])
def get_trip_suggestions():
    if request.method == "POST":
        preferences = request.json
        # Get the suggested trip based on the user’s preferences
        trip = Trip.get_trip(
            activity=preferences['activity'],
            travelMode=preferences['travelMode'],
            cost=preferences['cost'],
            carbonFootprint=preferences['carbonFootprint'],
            duration=preferences['duration']
        )

        # If a valid trip is found, return the trip data as a JSON response
        if trip:
            return jsonify({
                "name": trip.name,
                "activity": trip.activity,
                "destination": trip.destination,
                "cost": trip.cost,
                "carbonFootprint": trip.carbonFootprint,
                "duration": trip.duration,
                "travelMode": trip.travelMode
            }), 200
        else:
            # If no trip is found, return a message indicating failure
            return jsonify({"message": "No matching trip found."}), 404
    else:
        return jsonify({"message": "OPTIONS request received"}), 200  # Respond to OPTIONS requests


@main.route('/add_sample_trips', methods=['POST'])
def test_add_sample_trips():
    add_sample_trips()
    return {"message": "Sample trips added successfully!"}, 201
    

''' Example usage:
 curl -X POST http://localhost:5000/add_trip \
 -H "Content-Type: application/json" \
 -d '{"name": "Test activity in Test", "activity_type": "testing", "destination": "test", "cost": 123, "carbonFootprint": "testing", "duration": 2, "travelMode": "test"}'
'''
@main.route('/add_trip', methods=['POST'])
def add_trip():
    data = request.get_json()
    try:
        new_trip = Trip(
            name=data['name'],
            activity_type=data['activity_type'],
            destination=data['destination'],
            cost=data['cost'],
            carbonFootprint=data['carbonFootprint'],
            duration=data['duration'],
            travelMode=data['travelMode']
        )
        db.session.add(new_trip)
        db.session.commit()
        return {"message": "Trip added successfully!"}, 201
    except KeyError as e:
        return {"error": f"Missing field: {str(e)}"}, 400


@main.route('/api/trips', methods=['GET'])
def get_all_trips():
    trips = Trip.query.all()  # Get all trips from the database
    trips_list = [{"id": trip.id, "name": trip.name, "activity_type": trip.activity_type} for trip in trips]
    return jsonify(trips_list), 200


@main.route('/delete_trip/<int:id>', methods=['DELETE'])
def delete_trip(id):
    trip = Trip.query.get_or_404(id)
    db.session.delete(trip)
    db.session.commit()
    return {"message": f"Trip with id {id} deleted successfully!"}, 200
