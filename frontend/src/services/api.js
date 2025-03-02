import axios from 'axios';

const BASE_URL = 'http://localhost:5000'; // Ensure this matches your Flask backend setup

const axiosInstance = axios.create({
  baseURL: BASE_URL,
  timeout: 10000, // 10 seconds timeout
  headers: {
    'Content-Type': 'application/json',
  },
});

/**
 * Fetches trip suggestions from the backend API.
 * @param {Object} preferences - User-selected preferences for trip planning.
 * @returns {Object} - Trip suggestion data or an error message.
 */
export const fetchSuggestions = async (preferences) => {
  try {
    const response = await axiosInstance.post(
      '/api/trip-suggestions',
      preferences
    );
    return response.data;
  } catch (error) {
    console.error('API Request Failed:', error);

    // Handle different types of errors
    if (error.response) {
      // Server responded with a status other than 2xx
      console.error('Error Response Data:', error.response.data);
      console.error('Error Status:', error.response.status);
      return {
        error: `Server Error: ${error.response.status} - ${error.response.data.message || 'Unknown error'}`,
      };
    } else if (error.request) {
      // No response received from the server
      console.error('No response received from backend:', error.request);
      return {
        error:
          'Network error: No response from the server. Please check your connection.',
      };
    } else {
      // Other unexpected errors
      console.error('Unexpected Error:', error.message);
      return { error: 'Unexpected error occurred. Please try again later.' };
    }
  }
};
