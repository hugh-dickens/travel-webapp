/**
 * Displays the suggested trip based on user preferences.
 * Allows users to save a trip to the backend.
 */

import React, { useContext } from "react";
import { PreferencesContext } from "../context/PreferencesContext";
import "../styles/styles.css";

const TripSuggestions = () => {
  const { suggestions, error } = useContext(PreferencesContext);

  /**
   * Saves the suggested trip to the backend.
   * @param {Object} trip - The trip object to save.
   */
  const saveTrip = async (trip) => {
    try {
      const response = await fetch("/api/saved-trips", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ trip_id: trip.id }),
      });

      const data = await response.json();
      if (response.ok) {
        alert("Trip saved successfully!");
      } else {
        alert("Failed to save trip: " + data.error);
      }
    } catch (error) {
      alert("Error saving trip: " + error.message);
    }
  };

  return (
    <div className="container">
      <h2 className="text-center">Trip Suggestions</h2>

      {/* Display Error Message If API Fails */}
      {error && <p className="text-danger">{error}</p>}

      {/* Display Trip Data If Available */}
      {suggestions ? (
        <div className="row justify-content-center g-4">
          <div className="col-md-4">
            <div className="card h-100">
              <div className="card-body">
                <h5 className="card-title">{suggestions.name}</h5>
                <p className="card-text">
                  <strong>Destination:</strong> {suggestions.destination}
                </p>
                <p className="card-text">
                  <strong>Activity:</strong> {suggestions.activity}
                </p>
                <p className="card-text">
                  <strong>Cost:</strong> £{suggestions.cost}
                </p>
                <p className="card-text">
                  <strong>Carbon Footprint:</strong> {suggestions.carbonFootprint}
                </p>
                <p className="card-text">
                  <strong>Duration:</strong> {suggestions.duration} days
                </p>
                <p className="card-text">
                  <strong>Travel Mode:</strong> {suggestions.travelMode}
                </p>
                <a href="#" className="btn btn-success">
                  Explore
                </a>
                <button
                  className="btn btn-primary mx-2"
                  onClick={() => saveTrip(suggestions)}
                >
                  Save
                </button>
              </div>
            </div>
          </div>
        </div>
      ) : (
        <p className="text-muted">
          Please select preferences and submit to get a suggestion.
        </p>
      )}
    </div>
  );
};

export default TripSuggestions;
