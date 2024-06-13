/*
Form for users to input their travel preferences.
*/

import React, { useState, useContext } from 'react';
import { PreferencesContext } from '../context/PreferencesContext';

const PreferencesForm = () => {
  const { setPreferences } = useContext(PreferencesContext);
  const [activity, setActivity] = useState('');
  const [destination, setDestination] = useState('');
  const [travelMode, setTravelMode] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    setPreferences({ activity, destination, travelMode });
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Preferred Activity:</label>
        <select value={activity} onChange={(e) => setActivity(e.target.value)}>
          <option value="">Select Activity</option>
          <option value="rock climb">Rock Climbing</option>
          <option value="alpine climb">Alpine Climbing</option>
          <option value="mountain bike">Mountain Biking</option>
          <option value="hike">Hiking</option>
        </select>
      </div>
      <div>
        <label>Destination:</label>
        <select value={destination} onChange={(e) => setDestination(e.target.value)}>
          <option value="">Select Destination</option>
          <option value="Dolomites">Dolomites</option>
          <option value="Kalymnos">Kalymnos</option>
          <option value="Ailefroide">Ailefroide</option>
          <option value="Aosta valley">Aosta Valley</option>
        </select>
      </div>
      <div>
        <label>Travel Mode:</label>
        <select value={travelMode} onChange={(e) => setTravelMode(e.target.value)}>
          <option value="">Select Travel Mode</option>
          <option value="car">Car</option>
          <option value="plane">Plane</option>
          <option value="train">Train</option>
        </select>
      </div>
      <button type="submit">Get Suggestions</button>
    </form>
  );
};

export default PreferencesForm;
