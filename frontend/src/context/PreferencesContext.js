import React, { createContext, useState } from 'react';
import PropTypes from 'prop-types';

export const PreferencesContext = createContext();

export const PreferencesProvider = ({ children }) => {
  const [preferences, setPreferences] = useState({
    activity: '',
    destination: '',
    travelMode: '',
    cost: '',
    carbonFootprint: '',
    duration: '',
  });

  return (
    <PreferencesContext.Provider value={{ preferences, setPreferences }}>
      {children}
    </PreferencesContext.Provider>
  );
};

// Add prop type validation
PreferencesProvider.propTypes = {
  children: PropTypes.node.isRequired,
};
