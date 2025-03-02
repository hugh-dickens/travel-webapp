import unittest

from backend.app.trip_planner import Trip, TripPlanner


class TestTripPlanner(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up a sample list of trips for testing."""
        cls.sample_trips = [
            Trip(
                "Rock climbing in Kalymnos",
                "rock climb",
                "Kalymnos",
                1000,
                "low",
                7,
                "car",
            ),
            Trip(
                "Alpine climbing in Ailefroide",
                "alpine climb",
                "Ailefroide",
                2000,
                "medium",
                10,
                "train",
            ),
            Trip(
                "Mountain biking in Dolomites",
                "mountain bike",
                "Dolomites",
                1500,
                "low",
                5,
                "plane",
            ),
            Trip(
                "Hiking in Aosta Valley",
                "hike",
                "Aosta Valley",
                500,
                "extremely low",
                3,
                "train",
            ),
        ]
        cls.planner = TripPlanner(cls.sample_trips)

    def test_suggest_trip_exact_match(self):
        """Test if the planner finds an exact match based on user preferences."""
        trip = self.planner.suggest_trip(
            activity="rock climb",
            travel_mode="car",
            budget=1000,
            carbon_preference="low",
            duration=7,
        )
        self.assertIsNotNone(trip)
        self.assertEqual(trip.name, "Rock climbing in Kalymnos")

    def test_suggest_trip_flexible_duration(self):
        """Test if the planner suggests a trip when duration is slightly different."""
        trip = self.planner.suggest_trip(
            activity="hike",
            travel_mode="train",
            budget=600,
            carbon_preference="extremely low",
            duration=5,  # Duration is greater than available
        )
        self.assertIsNotNone(trip)
        self.assertEqual(trip.name, "Hiking in Aosta Valley")

    # TODO: again the no possible trip functionality is not implemented but should be in the future.
    # def test_suggest_trip_budget_limit(self):
    #     """Test if the planner avoids trips that exceed the budget."""
    #     trip = self.planner.suggest_trip(
    #         activity="alpine climb",
    #         travel_mode="train",
    #         budget=1000,  # Budget is too low for this trip
    #         carbon_preference="medium",
    #         duration=10
    #     )
    #     self.assertEqual(trip.name, "No suitable trip found")

    # def test_suggest_trip_no_results(self):
    #     """Test if the planner returns 'No suitable trip found' for no matches."""
    #     trip = self.planner.suggest_trip(
    #         activity="skiing",  # Activity not in sample list
    #         travel_mode="helicopter",
    #         budget=5000,
    #         carbon_preference="high",
    #         duration=14
    #     )
    #     self.assertEqual(trip.name, "No suitable trip found")

    def test_sort_by_duration(self):
        """Test sorting trips by duration (ascending)."""
        sorted_trips = self.planner.sort_by_duration(ascending=True)
        self.assertEqual(sorted_trips[0].name, "Hiking in Aosta Valley")
        self.assertEqual(sorted_trips[-1].name, "Alpine climbing in Ailefroide")

    def test_best_value_trip(self):
        """Test if the planner finds the best value trip based on cost per day."""
        best_trip = self.planner.best_value_trip()
        self.assertEqual(
            best_trip.name, "Rock climbing in Kalymnos"
        )  # Cheapest per day


if __name__ == "__main__":
    unittest.main()
