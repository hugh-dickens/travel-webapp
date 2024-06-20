import React, { createContext, useState } from 'react';

export const PreferencesContext = createContext();

export const PreferencesProvider = ({ children }) => {
  const [preferences, setPreferences] = useState({});
  const [suggestions, setSuggestions] = useState([]);

  return (
    <PreferencesContext.Provider value={{ preferences, setPreferences, suggestions, setSuggestions }}>
      {children}
    </PreferencesContext.Provider>
  );
};
