import unittest
from app import create_app, db
from app.models import Trip

class TestRoutes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Runs once before all tests."""
        cls.app = create_app()
        cls.app.config['TESTING'] = True
        # Use an in-memory SQLite database for testing - fast and isolated
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        cls.client = cls.app.test_client()
        with cls.app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        """Runs once after all tests."""
        with cls.app.app_context():
            db.session.remove()
            db.drop_all()

    def setUp(self):
        """Runs before each test."""
        with self.app.app_context():
            # Insert a sample trip
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
        """Runs after each test."""
        with self.app.app_context():
            db.session.query(Trip).delete()
            db.session.commit()

    def test_add_trip(self):
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
        self.assertIn("Trip added successfully!", response.get_json()['message'])

    def test_get_all_trips(self):
        response = self.client.get('/api/trips')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 1)  # One sample trip added in `setUp`
        self.assertEqual(data[0]['name'], "Test Trip")

    def test_delete_trip(self):
        # Get the ID of the sample trip added in `setUp`
        with self.app.app_context():
            trip = Trip.query.first()
            trip_id = trip.id

        response = self.client.delete(f'/delete_trip/{trip_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(f"Trip with id {trip_id} deleted successfully!", response.get_json()['message'])

    def test_get_trip_suggestions(self):
        response = self.client.post('/api/trip-suggestions', json={
            "activity": "hiking",
            "travelMode": "train",
            "cost": 200,
            "carbonFootprint": "medium",
            "duration": 3
        })
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)

    def test_add_sample_trips(self):
        response = self.client.post('/add_sample_trips')
        self.assertEqual(response.status_code, 201)
        self.assertIn("Sample trips added successfully!", response.get_json()['message'])

        with self.app.app_context():
            trips_count = Trip.query.count()
            self.assertGreater(trips_count, 1)  # Ensure sample trips are added
