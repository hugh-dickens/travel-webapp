"""
Setup the main routes for the application
"""

import traceback  # for debugging

from flask import Blueprint, jsonify, request

from backend.app.helpers import parse_range_or_value
from backend.app.models import Trip, SavedTrip, add_sample_trips, db
from backend.app.trip_planner import Trip, TripPlanner

# Assuming trip_planner is globally available
trip_planner = TripPlanner()

main = Blueprint("main", __name__)


@main.route("/api/trip-suggestions", methods=["POST"])
def get_trip_suggestions():
    """
    Gets a trip suggestion from the data sent by the frontend

    Expects a JSON request with:
        {
            ...
        }

    Returns:
        JSON response with a success message or an error.
    """
    try:
        preferences = request.json
        if not preferences:
            return jsonify({"error": "Missing JSON payload"}), 400

        required_keys = [
            "activity",
            "travelMode",
            "cost",
            "carbonFootprint",
            "duration",
        ]
        for key in required_keys:
            if key not in preferences:
                return jsonify({"error": f"Missing key in request: {key}"}), 400

        # Parse cost and duration from range strings
        cost_range = parse_range_or_value(preferences["cost"])
        duration_range = parse_range_or_value(preferences["duration"])

        if cost_range is None or duration_range is None:
            return jsonify({"error": "Invalid cost or duration range format"}), 400

        # Get the best trip suggestion using the TripPlanner logic
        trip = trip_planner.suggest_trip(
            activity=preferences["activity"],
            travel_mode=preferences["travelMode"],
            budget=cost_range[1],  # Max budget
            carbon_preference=preferences["carbonFootprint"].lower(),
            duration=duration_range[1],  # Max duration
        )

        if trip.name != "No suitable trip found":
            return (
                jsonify(
                    {
                        "name": trip.name,
                        "activity": trip.activity,
                        "destination": trip.destination,
                        "cost": trip.cost,
                        "carbonFootprint": trip.carbon_footprint,
                        "duration": trip.duration,
                        "travelMode": trip.travel_mode,
                    }
                ),
                200,
            )
        else:
            return jsonify({"message": "No matching trip found."}), 404

    except Exception as e:
        print("Error:", str(e))
        print(traceback.format_exc())
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500


@main.route("/api/saved-trips", methods=["POST"])
def save_trip():
    """
    Saves a trip for the single default user.

    Expects a JSON request with:
        {
            "trip_id": <trip_id>
        }

    Returns:
        JSON response with a success message or an error.
    """
    data = request.json
    if "trip_id" not in data:
        return jsonify({"error": "Missing trip_id"}), 400

    trip = Trip.query.get(data["trip_id"])
    if not trip:
        return jsonify({"error": "Trip not found"}), 404

    saved_trip = SavedTrip(trip_id=trip.id)
    db.session.add(saved_trip)
    db.session.commit()
    return jsonify({"message": "Trip saved successfully!", "trip": saved_trip.to_dict()}), 201


@main.route("/api/saved-trips", methods=["GET"])
def get_saved_trips():
    """
    Retrieves all saved trips for the single user.

    Returns:
        JSON list of saved trips.
    """
    trips = SavedTrip.query.all()
    return jsonify([trip.to_dict() for trip in trips])


""" Example usage:
 curl -X POST http://localhost:5000/add_trip \
 -H "Content-Type: application/json" \
 -d '{"name": "Test activity in Test", "activity_type": "testing", "destination": "test", "cost": 123, "carbonFootprint": "testing", "duration": 2, "travelMode": "test"}'
"""


@main.route("/add_trip", methods=["POST"])
def add_trip():
    data = request.get_json()
    try:
        new_trip = Trip(
            name=data["name"],
            activity_type=data["activity_type"],
            destination=data["destination"],
            cost=data["cost"],
            carbonFootprint=data["carbonFootprint"],
            duration=data["duration"],
            travelMode=data["travelMode"],
        )
        db.session.add(new_trip)
        db.session.commit()
        return {"message": "Trip added successfully!"}, 201
    except KeyError as e:
        return {"error": f"Missing field: {str(e)}"}, 400


@main.route("/api/trips", methods=["GET"])
def get_all_trips():
    trips = Trip.query.all()  # Get all trips from the database. Will need pagination eventually
    trips_list = [
        {"id": trip.id, "name": trip.name, "activity_type": trip.activity_type}
        for trip in trips
    ]
    return jsonify(trips_list), 200


@main.route("/delete_trip/<int:id>", methods=["DELETE"])
def delete_trip(id):
    trip = Trip.query.get_or_404(id)
    db.session.delete(trip)
    db.session.commit()
    return {"message": f"Trip with id {id} deleted successfully!"}, 200
