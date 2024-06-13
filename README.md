# Expedition Planner (to be renamed)

> **NOTE:** This project is in its early stages and is a work in progress. The current version focuses on the MVP requirements, and future updates will expand its functionality. The below also contains the INTENDED design and output of this project which is subject to change and iteration. It's merely here as a goal.

## Overview

Expedition Planner is a web application designed to help users plan outdoor activity-focused trips, such as climbing, running, mountaineering, and mountain biking. The application takes user preferences and suggests trips with different timespans, estimates costings, calculates carbon footprints, and determines the cost of required gear.

## MVP Requirements

The Minimum Viable Product (MVP) for Expedition Planner includes the following features:

1. **User Preferences Form**:
    - Collect user preferences for travel plans, including preferred activities, budget, location, duration, and other relevant details.

2. **Trip Suggestions**:
    - Based on user preferences, suggest trips with various timespans and activities.
    - Display basic information about each trip, including the destination, activity type, duration, and estimated cost.

3. **Cost Estimation**:
    - Provide an estimated cost for each suggested trip, including travel, accommodation, and activity costs.

4. **Carbon Footprint Calculation**:
    - Estimate the carbon footprint for each trip based on the mode of travel and distance.

5. **Gear Cost Calculation**:
    - Estimate the cost of any required gear for the trip based on the selected activities.

## Technologies Used (the fun stuff)

### Frontend

- **React**: A JavaScript library for building user interfaces. React will be used to create a responsive and dynamic user interface for the application.
- **Formik**: A library for building forms in React, which will be used for the user preferences form.
- **Axios**: A promise-based HTTP client for making API requests to the backend.
- **Styled-components**: A library for styling React components with CSS-in-JS.

### Backend

- **Python**: The backend of the application will be built using Python to handle API requests and perform the necessary calculations and data processing.
- **Flask**: A lightweight WSGI web application framework for Python, which will be used to create the API endpoints for handling user preferences and generating trip suggestions.
- **SQLAlchemy**: An SQL toolkit and Object-Relational Mapping (ORM) library for Python, which will be used to interact with the database.

### Other Tools

- **GitHub**: For version control and repository management.
- **Visual Studio Code**: Recommended IDE for development.
- **Postman**: For testing API endpoints.

## Setup and Installation

### Prerequisites

- Node.js and npm
- Python and pip

### Frontend Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/travel-webapp.git
    cd travel-webapp/frontend
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Start the development server:
    ```bash
    npm start
    ```

### Backend Setup

1. Navigate to the backend directory:
    ```bash
    cd ../backend
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Start the Flask server:
    ```bash
    python manage.py
    ```

## Usage

1. Open your browser and navigate to `http://localhost:3000` to access the frontend.
2. Fill in the user preferences form and submit it.
3. View the suggested trips, cost estimations, carbon footprint calculations, and gear cost calculations based on your preferences.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.


## Development help and tips

To create a new component in the frontend, the create-component.js file needs to be run:

```bash
pnpm run create-component MyNewComponent
```