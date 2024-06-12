/*
Form for users to input their travel preferences.
*/

import React, { useState } from 'react';
import { usePreferences } from '../context/PreferencesContext';

const PreferencesForm = () => {
  const { setPreferences } = usePreferences();
  const [formData, setFormData] = useState({
    activity: '',
    duration: '',
    budget: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setPreferences(formData);
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Activity:
        <input type="text" name="activity" value={formData.activity} onChange={handleChange} />
      </label>
      <label>
        Duration:
        <input type="text" name="duration" value={formData.duration} onChange={handleChange} />
      </label>
      <label>
        Budget:
        <input type="text" name="budget" value={formData.budget} onChange={handleChange} />
      </label>
      <button type="submit">Submit</button>
    </form>
  );
};

export default PreferencesForm;
