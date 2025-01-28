# config.py

import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://travel_user:fake_password@localhost:5432/travel_app")
