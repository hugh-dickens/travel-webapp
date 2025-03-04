/**
 * Displays the list of saved trips.
 */

import React, { useEffect, useState } from "react";

const SavedTrips = () => {
  const [savedTrips, setSavedTrips] = useState([]);

  useEffect(() => {
    /**
     * Fetches saved trips from the backend.
     */
    fetch("/api/saved-trips")
      .then((res) => res.json())
      .then((data) => setSavedTrips(data))
      .catch((error) => console.error("Error fetching saved trips:", error));
  }, []);

  return (
    <div className="container">
      <h2 className="text-center">Saved Trips</h2>
      {savedTrips.length > 0 ? (
        savedTrips.map((trip, index) => (
          <div key={index} className="card my-2">
            <div className="card-body">
              <h5 className="card-title">{trip.trip.name}</h5>
              <p><strong>Destination:</strong> {trip.trip.destination}</p>
              <p><strong>Activity:</strong> {trip.trip.activity}</p>
              <p><strong>Cost:</strong> £{trip.trip.cost}</p>
              <p><strong>Carbon Footprint:</strong> {trip.trip.carbonFootprint}</p>
              <p><strong>Duration:</strong> {trip.trip.duration} days</p>
              <p><strong>Travel Mode:</strong> {trip.trip.travelMode}</p>
            </div>
          </div>
        ))
      ) : (
        <p className="text-muted">No saved trips yet.</p>
      )}
    </div>
  );
};

export default SavedTrips;
