/*
Display the list of trip suggestions based on user preferences.
*/

import React, { useContext } from 'react';
import { PreferencesContext } from '../context/PreferencesContext';

const TripSuggestions = () => {
  const { preferences } = useContext(PreferencesContext);

  const getSuggestion = () => {
    if (preferences.destination && preferences.travelMode) {
      return `We suggest you go to ${preferences.destination} by ${preferences.travelMode}, if you would like to ${preferences.activity}.`;
    }
    return 'Please select preferences to get a suggestion.';
  };

  return (
    <div>
      <h2>Trip Suggestions</h2>
      <p>{getSuggestion()}</p>
    </div>
  );
};

export default TripSuggestions;

