import React, { createContext, useState } from 'react';

export const PreferencesContext = createContext();

export const PreferencesProvider = ({ children }) => {
  const [preferences, setPreferences] = useState({});
  const [suggestions, setSuggestions] = useState(null);
  const [error, setError] = useState(null);

  return (
    <PreferencesContext.Provider
      value={{
        preferences,
        setPreferences,
        suggestions,
        setSuggestions,
        error,
        setError,
      }}
    >
      {children}
    </PreferencesContext.Provider>
  );
};
