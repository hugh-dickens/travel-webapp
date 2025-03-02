"""
Module for calculating and recommending trips based on user inputs.
"""

from typing import List, Optional


class Trip:
    """Represents a trip with relevant attributes."""

    def __init__(
        self,
        name: str,
        activity: str,
        destination: str,
        cost: float,
        carbon_footprint: str,
        duration: int,
        travel_mode: str,
    ):
        self.name = name
        self.activity = activity
        self.destination = destination
        self.cost = cost
        self.carbon_footprint = carbon_footprint
        self.duration = duration
        self.travel_mode = travel_mode

    @classmethod
    def get_trip(cls, activity, travelMode, cost, carbonFootprint, duration):
        # Logic to find a trip based on provided preferences
        # Return a matching Trip object or None if no match
        matching_trip = None
        for trip in sample_trips:
            if (
                trip["activity"] == activity
                and trip["travelMode"] == travelMode
                and trip["cost"] <= cost
                and trip["carbonFootprint"] == carbonFootprint
                and trip["duration"] <= duration
            ):
                matching_trip = cls(**trip)
                break
        return matching_trip

    def cost_per_day(self) -> float:
        """Calculates the cost per day for a trip."""
        return self.cost / self.duration if self.duration > 0 else float("inf")

    def __repr__(self):
        return f"Trip({self.name}, {self.destination}, {self.activity}, {self.cost:.2f}, {self.carbon_footprint}, {self.duration}, {self.travel_mode})"


class TripPlanner:
    """Handles trip suggestions and additional filtering/sorting functionalities."""

    def __init__(self, trips: Optional[List[Trip]] = None):
        """
        Initializes the TripPlanner with a list of trips.
        If no trips are provided, default sample trips are used.
        """
        if trips is None:
            self.trips = self.default_trips()
        else:
            self.trips = trips

    @staticmethod
    def default_trips() -> List[Trip]:
        """Returns a default list of sample trips."""
        return [
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

    def suggest_trip(
        self,
        activity: str,
        travel_mode: str,
        budget: int,
        carbon_preference: str,
        duration: int,
    ) -> Trip:
        """Suggests a trip based on user preferences using a scoring system."""
        best_trip = None
        best_score = -1

        for trip in self.trips:
            score = 0

            if trip.activity == activity:
                score += 3
            if trip.travel_mode == travel_mode:
                score += 2
            if trip.cost <= budget:
                score += 2
            if trip.carbon_footprint == carbon_preference:
                score += 2
            if abs(trip.duration - duration) <= 2:
                score += 1

            if score > best_score:
                best_trip = trip
                best_score = score

        return (
            best_trip
            if best_trip
            else Trip("No suitable trip found", "", "", 0, "", 0, "")
        )

    def filter_by_budget(self, max_budget: float) -> List[Trip]:
        """Returns a list of trips that fit within a given budget."""
        return [trip for trip in self.trips if trip.cost <= max_budget]

    def most_eco_friendly_trips(self, top_n: int = 3) -> List[Trip]:
        """Returns the most eco-friendly trips (prioritizing lowest carbon footprint)."""
        eco_ranking = {"extremely low": 3, "low": 2, "medium": 1, "high": 0}
        return sorted(
            self.trips,
            key=lambda trip: eco_ranking.get(trip.carbon_footprint, 0),
            reverse=True,
        )[:top_n]

    def sort_by_duration(self, ascending: bool = True) -> List[Trip]:
        """Sorts trips by duration, either shortest to longest or vice versa."""
        return sorted(self.trips, key=lambda trip: trip.duration, reverse=not ascending)

    def best_value_trip(self) -> Trip:
        """Finds the best trip based on cost per day (lowest cost per day is better)."""
        return min(self.trips, key=lambda trip: trip.cost_per_day(), default=None)

    def recommend_based_on_past_choices(self, past_trips: List[Trip]) -> Optional[Trip]:
        """Suggests a trip based on previous user choices by matching activity and travel mode."""
        if not past_trips:
            return None

        # Find most frequent activity and travel mode from past choices
        activity_count = {}
        travel_mode_count = {}

        for trip in past_trips:
            activity_count[trip.activity] = activity_count.get(trip.activity, 0) + 1
            travel_mode_count[trip.travel_mode] = (
                travel_mode_count.get(trip.travel_mode, 0) + 1
            )

        most_common_activity = max(activity_count, key=activity_count.get)
        most_common_travel_mode = max(travel_mode_count, key=travel_mode_count.get)

        # Recommend a trip that matches these preferences
        for trip in self.trips:
            if (
                trip.activity == most_common_activity
                and trip.travel_mode == most_common_travel_mode
            ):
                return trip

        return None  # No exact match found


# Example usage
if __name__ == "__main__":
    planner = TripPlanner()

    print(
        "Suggested Trip:",
        planner.suggest_trip(
            activity="hike",
            travel_mode="train",
            budget=600,
            carbon_preference="extremely low",
            duration=3,
        ),
    )
    print("Trips under $800:", planner.filter_by_budget(800))
    print("Most eco-friendly trips:", planner.most_eco_friendly_trips())
    print("Trips sorted by duration (shortest first):", planner.sort_by_duration())
    print("Best value trip:", planner.best_value_trip())

    past_choices = [
        Trip(
            "Alpine climbing in Ailefroide",
            "alpine climb",
            "Ailefroide",
            2000 / 10,
            "medium",
            10,
            "train",
        ),
        Trip(
            "Rock climbing in Kalymnos",
            "rock climb",
            "Kalymnos",
            1000 / 7,
            "low",
            7,
            "car",
        ),
    ]
    print(
        "Recommended based on past choices:",
        planner.recommend_based_on_past_choices(past_choices),
    )
