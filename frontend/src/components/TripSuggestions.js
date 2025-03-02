/*
Display the list of trip suggestions based on user preferences.
*/

import React, { useContext } from 'react';
import { PreferencesContext } from '../context/PreferencesContext';
import '../styles/styles.css';

const TripSuggestions = () => {
  const { suggestions, error } = useContext(PreferencesContext);

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
                  <strong>Carbon Footprint:</strong>{' '}
                  {suggestions.carbonFootprint}
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
                <button className="btn btn-primary mx-2">Save</button>
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
