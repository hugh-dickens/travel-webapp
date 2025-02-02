import unittest
from app.trip_planner import Trip, TripPlanner  # Adjust import as per your module structure

class TestTripPlanner(unittest.TestCase):

    def setUp(self):
        """Initialize the sample trip data before each test."""
        self.sample_trips = [
            Trip("Rock climbing in Kalymnos", "rock climb", "Kalymnos", 1000 / 7, "low", 7, "car"),
            Trip("Alpine climbing in Ailefroide", "alpine climb", "Ailefroide", 2000 / 10, "medium", 10, "train"),
            Trip("Mountain biking in Dolomites", "mountain bike", "Dolomites", 1500 / 5, "low", 5, "plane"),
            Trip("Hiking in Aosta Valley", "hike", "Aosta Valley", 500 / 3, "extremely low", 3, "train"),
        ]
        self.planner = TripPlanner(self.sample_trips)

    def test_suggest_trip(self):
        """Test the trip suggestion logic based on preferences."""
        suggested_trip = self.planner.suggest_trip(
            activity="hike", travel_mode="train", budget=600, carbon_preference="extremely low", duration=3
        )
        self.assertEqual(suggested_trip.name, "Hiking in Aosta Valley")
        self.assertEqual(suggested_trip.destination, "Aosta Valley")

    def test_filter_by_budget(self):
        """Test filtering trips by budget."""
        filtered_trips = self.planner.filter_by_budget(800)
        self.assertEqual(len(filtered_trips), 4)  # Expecting 4 trips under $800, adjust if necessary
        self.assertTrue(all(trip.cost <= 800 for trip in filtered_trips))

    def test_most_eco_friendly_trips(self):
        """Test sorting trips based on eco-friendliness."""
        eco_trips = self.planner.most_eco_friendly_trips()
        self.assertEqual(eco_trips[0].name, "Hiking in Aosta Valley")  # Expected eco-friendly trip

    def test_sort_by_duration(self):
        """Test sorting trips by duration."""
        sorted_trips = self.planner.sort_by_duration(ascending=True)
        self.assertEqual(sorted_trips[0].name, "Hiking in Aosta Valley")
        self.assertEqual(sorted_trips[-1].name, "Alpine climbing in Ailefroide")

    def test_best_value_trip(self):
        """Test finding the best value trip based on cost per day."""
        best_value_trip = self.planner.best_value_trip()
        self.assertEqual(best_value_trip.name, "Alpine climbing in Ailefroide")  # Adjusted based on cost per day comparison

    def test_recommend_based_on_past_choices(self):
        """Test recommending a trip based on past choices."""
        past_choices = [
            Trip("Alpine climbing in Ailefroide", "alpine climb", "Ailefroide", 2000 / 10, "medium", 10, "train"),
            Trip("Rock climbing in Kalymnos", "rock climb", "Kalymnos", 1000 / 7, "low", 7, "car"),
        ]
        recommended_trip = self.planner.recommend_based_on_past_choices(past_choices)
        self.assertEqual(recommended_trip.name, "Alpine climbing in Ailefroide")  # Adjusted based on frequency

if __name__ == '__main__':
    unittest.main()
