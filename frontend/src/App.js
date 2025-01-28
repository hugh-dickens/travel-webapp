import React from 'react';
import { PreferencesProvider } from './context/PreferencesContext';
import PreferencesForm from './components/PreferencesForm';
import TripSuggestions from './components/TripSuggestions';
import './styles.css';

const App = () => (
  <PreferencesProvider>
    <div className="styles">
      <PreferencesForm />
      <TripSuggestions />
    </div>
  </PreferencesProvider>
);

export default App;
