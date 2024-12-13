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

failed_suggestion = [
    {"name": "Failed to find a suggestion", "activity": "", "destination": "", "cost": 0, "carbonFootprint": "", "duration": 0, "travelMode": ""},
]

def get_trip(activity, travelMode, cost, carbonFootprint, duration):
    # add some internal logic to choose a trip here

    # create a score for the input and suggest a trip based on this
    trip_score = []
    res = failed_suggestion

    # replace the below if statements with a "find" to locate the indexes with these dictionary inputs
    # store the indexes in a list and at the end return the best index
    if activity == "rock climb":
        trip_score.append(0)
    if activity == "alpine climb":
        trip_score.append(1)
    elif activity == "mountain bike":
        trip_score.append(2)
    elif activity == "hike":
        trip_score.append(3)
    else:
        pass

    if travelMode == "car":
        trip_score.append(0)
    elif travelMode == "train":
        trip_score.append(1)
        trip_score.append(3)
    elif travelMode == "plane":
        trip_score.append(2)
    else:
        pass
    
    # FIXME: comes in as £1000-£2000 think this should be changed on the frontend to just
    # give integer numbers here or need to decode them
    # cost = int(cost)
    # if cost < 501:
    #     trip_score.append(3)
    # elif cost < 1001:
    #     trip_score.append(0)
    # elif cost < 1501:
    #     trip_score.append(2)
    # elif cost < 2001:
    #     trip_score.append(1)
    # else:
    #     pass

    trip_score = max(trip_score) # TODO this just returns the max number in the list

    return sample_trips[trip_score]