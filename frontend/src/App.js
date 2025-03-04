/**
 * Main application component that manages navigation and pages.
 */

import React from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import PreferencesForm from "./components/PreferencesForm";
import TripSuggestions from "./components/TripSuggestions";
import SavedTrips from "./components/SavedTrips"; // Import the saved trips component
import "./styles/styles.css";

const App = () => {
  return (
    <Router>
      <div>
        {/* Header */}
        <header className="bg-primary text-white py-4">
          <div className="container d-flex justify-content-between align-items-center">
            <Link to="/" className="text-white text-decoration-none">
              Home
            </Link>
            <h1 className="display-4 mx-auto">Expedition Planner</h1>
            <Link to="/trips" className="text-white text-decoration-none">
              Saved Trips
            </Link>
          </div>
        </header>

        <div className="container text-center my-5">
          <p className="fs-4">
            Discover amazing adventures and plan your expeditions with ease.
          </p>
        </div>

        {/* Page Routing */}
        <Routes>
          {/* Home Page */}
          <Route
            path="/"
            element={
              <>
                <div className="container my-4">
                  <PreferencesForm />
                </div>
                <div className="container my-4">
                  <TripSuggestions />
                </div>
              </>
            }
          />

          {/* Saved Trips Page */}
          <Route path="/trips" element={<SavedTrips />} />
        </Routes>

        {/* Footer */}
        <footer className="bg-dark text-white text-center py-3 mt-5">
          <p>© 2025 Expedition Planner. All rights reserved.</p>
        </footer>
      </div>
    </Router>
  );
};

export default App;
