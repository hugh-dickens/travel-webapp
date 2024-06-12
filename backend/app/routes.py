from flask import Blueprint, request, jsonify

main = Blueprint('main', __name__)

@main.route('/api/trip-suggestions', methods=['POST'])
def get_trip_suggestions():
    preferences = request.json
    # Simulate trip suggestions
    trips = [
        {"name": "Mountain Climbing in Alps", "cost": "$2000"},
        {"name": "Hiking in Andes", "cost": "$1500"}
    ]
    return jsonify(trips)
