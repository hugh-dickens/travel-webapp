// frontend/src/services/api.js

import axios from 'axios';

const BASE_URL = 'http://localhost:5000';  // Adjust the port as per your Flask backend setup

const axiosInstance = axios.create({
  baseURL: BASE_URL,
  timeout: 10000,  // Adjust timeout if necessary
  headers: {
    'Content-Type': 'application/json',
  },
});

export const fetchSuggestions = async (preferences) => {
  try {
    const response = await axiosInstance.post('/api/trip-suggestions', preferences);
    
    return response.data;
  } catch (error) {
    throw error;  // currently no error handling strategy
  }
};
