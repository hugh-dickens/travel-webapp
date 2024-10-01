"""
file containing methods to calculate a suggested trip based on inputs
"""

# Sample trip data
sample_trips = [
    {"name": "Rock climbing in Kalymnos", "activity": "rock climb", "destination": "Kalymnos", "cost": 1000/7, "carbonFootprint": "low", "duration": 7, "travelMode": "car"},
    {"name": "Alpine climbing in Ailefroide", "activity": "alpine climb", "destination": "Ailefroide", "cost": 2000/10, "carbonFootprint": "medium", "duration": 10, "travelMode": "train"},
    {"name": "Mountain biking in Dolomites", "activity": "mountain bike", "destination": "Dolomites", "cost": 1500/5, "carbonFootprint": "low", "duration": 5, "travelMode": "plane"},
    {"name": "Hiking in Aosta Valley", "activity": "hike", "destination": "Aosta Valley", "cost": 500/3, "carbonFootprint": "extremely low", "duration": 3, "travelMode": "train"},
]

def get_trip(activity, destination, travelMode, cost, carbonFootprint, duration):
    # add some internal logic to choose a trip here
    return sample_trips[2]