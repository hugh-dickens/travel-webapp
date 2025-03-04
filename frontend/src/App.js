import React from 'react';
import PreferencesForm from './components/PreferencesForm';
import TripSuggestions from './components/TripSuggestions';
import './styles/styles.css';
import bannerImage from "./assets/BackgroundBanner.jpg";

const App = () => {
  return (
    <div>
      {/* Header Banner */}
      <header
        className="banner"
        style={{ backgroundImage: `url(${bannerImage})` }}
      >
        <div className="overlay">
          <div className="container d-flex justify-content-between align-items-center">
            <a href="/" className="text-white text-decoration-none">
              Home
            </a>
            <h1 className="display-4 mx-auto">Expedition Planner</h1>
            <a href="/trips" className="text-white text-decoration-none">
              Saved Trips
            </a>
          </div>
        </div>
      </header>

      <div className="container text-center my-5">
        <p className="fs-4">
          Discover amazing adventures and plan your expeditions with ease.
        </p>
      </div>

      {/* Preferences Form Section */}
      <div className="container my-4">
        <PreferencesForm />
      </div>

      {/* Trip Suggestions Section */}
      <div className="container my-4">
        <TripSuggestions />
      </div>

      {/* Footer */}
      <footer className="bg-dark text-white text-center py-3 mt-5">
        <p>© 2025 Expedition Planner. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default App;
