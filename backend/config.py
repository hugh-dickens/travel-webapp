# config.py

import os

# This is not a security risk. It is FAKE and does not exist other than for basic testing
DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://travel_user:fake_password@localhost:5432/travel_app"
)
