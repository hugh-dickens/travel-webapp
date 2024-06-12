/*
Display the list of trip suggestions based on user preferences.
*/

import React, { useEffect, useState } from 'react';
import { usePreferences } from '../context/PreferencesContext';
import axios from 'axios';

const TripSuggestions = () => {
  const { preferences } = usePreferences();
  const [trips, setTrips] = useState([]);

  useEffect(() => {
    if (preferences) {
      axios.post('http://localhost:5000/api/trip-suggestions', preferences)
        .then(response => {
          setTrips(response.data);
        })
        .catch(error => {
          console.error('Error fetching trip suggestions:', error);
        });
    }
  }, [preferences]);

  return (
    <div>
      <h2>Trip Suggestions</h2>
      <ul>
        {trips.map((trip, index) => (
          <li key={index}>{trip.name} - {trip.cost}</li>
        ))}
      </ul>
    </div>
  );
};

export default TripSuggestions;
