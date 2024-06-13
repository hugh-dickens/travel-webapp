import React, { createContext, useState } from 'react';

export const PreferencesContext = createContext();

export const PreferencesProvider = ({ children }) => {
  const [preferences, setPreferences] = useState({ activity: '', destination: '', travelMode: '' });

  return (
    <PreferencesContext.Provider value={{ preferences, setPreferences }}>
      {children}
    </PreferencesContext.Provider>
  );
};

