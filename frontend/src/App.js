import React from 'react';
import { PreferencesProvider } from './context/PreferencesContext';
import PreferencesForm from './components/PreferencesForm';
import TripSuggestions from './components/TripSuggestions';
import './styles.css';

const App = () => (
  <PreferencesProvider>
    <div className="styles">
      <h1>Expedition Planner</h1>
      <PreferencesForm />
      <TripSuggestions />
    </div>
  </PreferencesProvider>
);

export default App;
