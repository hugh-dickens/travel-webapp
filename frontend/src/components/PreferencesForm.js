/*
Form for users to input their travel preferences.
*/
// frontend/src/components/PreferencesForm.js

import React, { useState, useContext } from 'react';
import { PreferencesContext } from '../context/PreferencesContext';
import { fetchSuggestions } from '../services/api';

const PreferencesForm = () => {
  const { setPreferences, setSuggestions } = useContext(PreferencesContext);
  const [activity, setActivity] = useState('');
  const [destination, setDestination] = useState('');
  const [travelMode, setTravelMode] = useState('');
  const [cost, setCost] = useState('');
  const [carbonFootprint, setCarbonFootprint] = useState('');
  const [duration, setDuration] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const preferences = { activity, destination, travelMode, cost, carbonFootprint, duration };
    try {
      const suggestions = await fetchSuggestions(preferences);  // Use fetchSuggestions function
      setSuggestions(suggestions);  // Update suggestions in the context
      console.log('Received suggestions:', suggestions);
    } catch (error) {
      console.error('Error fetching suggestions:', error);
    }
    setPreferences(preferences);  // Update preferences in the context
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
        <label>Travel Mode:</label>
        <select
          value={travelMode}
          onChange={(e) => setTravelMode(e.target.value)}
        >
          <option value="">Select Travel Mode</option>
          <option value="car">Car</option>
          <option value="plane">Plane</option>
          <option value="train">Train</option>
        </select>
      </div>
      <div>
        <label>Cost:</label>
        <select value={cost} onChange={(e) => setCost(e.target.value)}>
          <option value="">Select Cost</option>
          <option value="<£1000">{'<'}£1000</option>
          <option value="£1000-£2000">£1000-£2000</option>
          <option value="£2000-£4000">£2000-£4000</option>
          <option value=">£4000">{'>'}£4000</option>
        </select>
      </div>
      <div>
        <label>Carbon Footprint:</label>
        <select
          value={carbonFootprint}
          onChange={(e) => setCarbonFootprint(e.target.value)}
        >
          <option value="">Select Carbon Footprint</option>
          <option value="extremely low">Extremely Low</option>
          <option value="low">Low</option>
          <option value="medium">Medium</option>
        </select>
      </div>
      <div>
        <label>Duration of Trip:</label>
        <select value={duration} onChange={(e) => setDuration(e.target.value)}>
          <option value="">Select Duration</option>
          <option value="1-7 days">1-7 days</option>
          <option value="7-14 days">7-14 days</option>
          <option value="2-4 weeks">2-4 weeks</option>
          <option value="1-3 months">1-3 months</option>
        </select>
      </div>
      <button type="submit">Get Suggestions</button>
    </form>
  );
};

export default PreferencesForm;
