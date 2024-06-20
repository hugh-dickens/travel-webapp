"""
Setup the main routes for the application
"""

from flask import Blueprint, request, jsonify

main = Blueprint("main", __name__)

# Sample trip data
sample_trips = [
    {"name": "Rock climbing in Kalymnos", "activity": "rock climb", "destination": "Kalymnos", "cost": 1000/7, "carbonFootprint": "low", "duration": 7, "travelMode": "car"},
    {"name": "Alpine climbing in Ailefroide", "activity": "alpine climb", "destination": "Ailefroide", "cost": 2000/10, "carbonFootprint": "medium", "duration": 10, "travelMode": "train"},
    {"name": "Mountain biking in Dolomites", "activity": "mountain bike", "destination": "Dolomites", "cost": 1500/5, "carbonFootprint": "low", "duration": 5, "travelMode": "plane"},
    {"name": "Hiking in Aosta Valley", "activity": "hike", "destination": "Aosta Valley", "cost": 500/3, "carbonFootprint": "extremely low", "duration": 3, "travelMode": "train"},
]

@main.route("/api/trip-suggestions", methods=["POST"])
def get_trip_suggestions():
    if request.method == "POST":
        preferences = request.json
        # Simulate trip suggestions (replace with your actual logic)
        trips = [
            sample_trips[2]
        ]
        return jsonify(trips)
    else:
        return jsonify({"message": "OPTIONS request received"}), 200  # Respond to OPTIONS requests

