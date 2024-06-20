/*
Display the list of trip suggestions based on user preferences.
*/

import React, { useContext } from 'react';
import { PreferencesContext } from '../context/PreferencesContext';

const TripSuggestions = () => {
  const { suggestions } = useContext(PreferencesContext);

  return (
    <div>
      <h2>Trip Suggestions</h2>
      {suggestions.length > 0 ? (
        suggestions.map((trip, index) => (
          <div key={index} style={{ marginBottom: '10px' }}>
            <strong>{trip.name}</strong>
            <p>
              Cost: £{trip.cost} average per day<br />
              Carbon Footprint: {trip.carbonFootprint}
            </p>
          </div>
        ))
      ) : (
        <p>Please select preferences to get a suggestion.</p>
      )}
    </div>
  );
};

export default TripSuggestions;

