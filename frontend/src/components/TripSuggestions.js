/*
Display the list of trip suggestions based on user preferences.
*/

import React, { useContext, useEffect, useState } from 'react';
import { PreferencesContext } from '../context/PreferencesContext';
import axios from 'axios';

const TripSuggestions = () => {
  const { preferences } = useContext(PreferencesContext);
  const [suggestions, setSuggestions] = useState([]);

  useEffect(() => {
    const fetchSuggestions = async () => {
      try {
        console.log('Fetching suggestions with preferences:', preferences);
        const response = await axios.post('/api/trip-suggestions', preferences);
        console.log('Suggestions received:', response.data);
        setSuggestions(response.data);
      } catch (error) {
        console.error('Error fetching trip suggestions:', error);
      }
    };

    if (preferences && Object.keys(preferences).length > 0) {
      fetchSuggestions();
    }
  }, [preferences]);

  const renderSuggestions = () => {
    if (suggestions.length === 0) {
      return <p>No suggestions available.</p>;
    }

    return (
      <ul>
        {suggestions.map((trip, index) => (
          <li key={index}>
            {trip.name}: {trip.cost}
          </li>
        ))}
      </ul>
    );
  };

  return (
    <div>
      <h2>Trip Suggestions</h2>
      <p>{renderSuggestions()}</p>
    </div>
  );
};

export default TripSuggestions;

