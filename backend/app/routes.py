"""
Setup the main routes for the application
"""

from flask import Blueprint, request, jsonify
from flask_cors import cross_origin # useful in DEV but should be removed if ever in production

main = Blueprint("main", __name__)

# Sample trip data
sample_trips = [
    {"name": "Rock Climbing in Dolomites", "activity": "rock climb", "destination": "Dolomites", "cost": 1000, "carbonFootprint": "low", "duration": 7, "travelMode": "car"},
    {"name": "Alpine Climbing in Alps", "activity": "alpine climb", "destination": "Aosta valley", "cost": 2000, "carbonFootprint": "medium", "duration": 10, "travelMode": "train"},
    {"name": "Mountain Biking in Kalymnos", "activity": "mountain bike", "destination": "Kalymnos", "cost": 1500, "carbonFootprint": "low", "duration": 5, "travelMode": "plane"},
    {"name": "Hiking in Ailefroide", "activity": "hike", "destination": "Ailefroide", "cost": 500, "carbonFootprint": "extremely low", "duration": 3, "travelMode": "train"},
]

@main.route("/api/trip-suggestions", methods=["POST", "OPTIONS"])
@cross_origin()  # Apply cross_origin decorator
def get_trip_suggestions():
    if request.method == "POST":
        preferences = request.json
        # Simulate trip suggestions (replace with your actual logic)
        trips = [
            sample_trips[1]
        ]
        return jsonify(trips)
    else:
        return jsonify({"message": "OPTIONS request received"}), 200  # Respond to OPTIONS requests

