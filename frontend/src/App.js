import React from 'react';
import { PreferencesProvider } from './context/PreferencesContext';
import PreferencesForm from './components/PreferencesForm';
import TripSuggestions from './components/TripSuggestions';

const App = () => (
  <PreferencesProvider>
    <div className="App">
      <h1>Travel Planner</h1>
      <PreferencesForm />
      <TripSuggestions />
    </div>
  </PreferencesProvider>
);

export default App;
