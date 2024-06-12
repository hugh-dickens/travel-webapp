import React, { createContext, useContext, useState } from 'react';

const PreferencesContext = createContext();

export const PreferencesProvider = ({ children }) => {
  const [preferences, setPreferences] = useState(null);

  return (
    <PreferencesContext.Provider value={{ preferences, setPreferences }}>
      {children}
    </PreferencesContext.Provider>
  );
};

export const usePreferences = () => useContext(PreferencesContext);
