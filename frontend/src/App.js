import React from 'react';
import { PreferencesProvider } from './context/PreferencesContext';
import PreferencesForm from './components/PreferencesForm';
import TripSuggestions from './components/TripSuggestions';
import './App.css';

const App = () => (
  <PreferencesProvider>
    <div className="App">
      <h1>Expedition Planner</h1>
      <PreferencesForm />
      <TripSuggestions />
    </div>
  </PreferencesProvider>
);

export default App;
