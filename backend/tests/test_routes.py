import unittest
from backend.app import create_app, db
from backend.app.models import Trip

class TestRoutes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Runs once before all tests to set up the test app and database."""
        cls.app = create_app()
        cls.app.config['TESTING'] = True
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory DB for fast testing
        cls.client = cls.app.test_client()

        with cls.app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        """Runs once after all tests to clean up the database."""
        with cls.app.app_context():
            db.session.remove()
            db.drop_all()

    def setUp(self):
        """Runs before each test to insert a sample trip."""
        with self.app.app_context():
            trip = Trip(
                name="Test Trip",
                activity_type="test",
                destination="Test Destination",
                cost=100.0,
                carbonFootprint="low",
                duration=2,
                travelMode="car"
            )
            db.session.add(trip)
            db.session.commit()

    def tearDown(self):
        """Runs after each test to clean up the database."""
        with self.app.app_context():
            db.session.query(Trip).delete()
            db.session.commit()

    def test_add_trip(self):
        """Test if a trip can be added successfully."""
        response = self.client.post('/add_trip', json={
            "name": "New Trip",
            "activity_type": "hiking",
            "destination": "Mountains",
            "cost": 200,
            "carbonFootprint": "medium",
            "duration": 3,
            "travelMode": "train"
        })
        self.assertEqual(response.status_code, 201)
        json_data = response.get_json()
        self.assertIn("Trip added successfully!", json_data['message'])

        # Verify trip was added
        with self.app.app_context():
            trip_count = Trip.query.count()
            self.assertEqual(trip_count, 2)  # One pre-existing trip + one new trip

    def test_get_all_trips(self):
        """Test fetching all trips."""
        response = self.client.get('/api/trips')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()

        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 1)  # At least one trip exists
        self.assertEqual(data[0]['name'], "Test Trip")

    def test_delete_trip(self):
        """Test deleting a trip by its ID."""
        with self.app.app_context():
            trip = Trip.query.first()
            trip_id = trip.id

        response = self.client.delete(f'/delete_trip/{trip_id}')
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertIn(f"Trip with id {trip_id} deleted successfully!", json_data['message'])

        # Verify trip was deleted
        with self.app.app_context():
            deleted_trip = db.session.get(Trip, trip_id)
            self.assertIsNone(deleted_trip)

    def test_get_trip_suggestions(self):
        """Test the trip suggestion endpoint."""
        response = self.client.post('/api/trip-suggestions', json={
            "activity": "test",
            "travelMode": "car",
            "cost": 100,
            "carbonFootprint": "low",
            "duration": 2
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, dict)
        self.assertGreaterEqual(len(data), 1)  # At least one trip should match

    # TODO: the below is some functionality that isnt currently implemented but should be in a future version of this application.
    # At the moment we always return a suggestion even if none should exist
    # def test_get_trip_suggestions_no_match(self):
    #     """Test trip suggestion endpoint with no matching trips."""
    #     response = self.client.post('/api/trip-suggestions', json={
    #         "activity": "skiing",  # No trip should match skiing
    #         "travelMode": "helicopter",
    #         "cost": 5000,
    #         "carbonFootprint": "high",
    #         "duration": 14
    #     })
    #     self.assertEqual(response.status_code, 404)
    #     json_data = response.get_json()
    #     self.assertIn("No matching trip found.", json_data['message'])

    def test_add_sample_trips(self):
        """Test adding multiple sample trips."""
        response = self.client.post('/add_sample_trips')
        self.assertEqual(response.status_code, 201)
        json_data = response.get_json()
        self.assertIn("Sample trips added successfully!", json_data['message'])

        with self.app.app_context():
            trips_count = Trip.query.count()
            self.assertGreater(trips_count, 1)  # Ensure sample trips are added

if __name__ == "__main__":
    unittest.main()

