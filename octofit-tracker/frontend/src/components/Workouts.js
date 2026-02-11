import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
    
    console.log('Workouts - Fetching from:', apiUrl);
    
    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Workouts - Raw data received:', data);
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        console.log('Workouts - Processed data:', workoutsData);
        setWorkouts(workoutsData);
        setLoading(false);
      })
      .catch(error => {
        console.error('Workouts - Error fetching:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return (
    <div className="container mt-4">
      <div className="loading-message">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
        <p className="mt-3">Loading workouts...</p>
      </div>
    </div>
  );
  
  if (error) return (
    <div className="container mt-4">
      <div className="alert alert-danger" role="alert">
        <h4 className="alert-heading">Error!</h4>
        <p>{error}</p>
      </div>
    </div>
  );

  return (
    <div className="container mt-4">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2 className="mb-0">💪 Suggested Workouts</h2>
        <span className="badge bg-danger">{workouts.length} Available</span>
      </div>
      <div className="row">
        {workouts.length > 0 ? (
          workouts.map(workout => (
            <div key={workout.id} className="col-md-6 mb-4">
              <div className="card h-100 border-danger">
                <div className="card-header bg-danger text-white">
                  <h5 className="card-title mb-0 text-white">{workout.name}</h5>
                </div>
                <div className="card-body">
                  <p className="card-text">{workout.description}</p>
                  <hr />
                  <div className="row g-2">
                    <div className="col-6">
                      <span className="badge bg-secondary w-100">📝 {workout.workout_type}</span>
                    </div>
                    <div className="col-6">
                      <span className="badge bg-warning text-dark w-100">⚡ {workout.difficulty_level}</span>
                    </div>
                    <div className="col-6">
                      <span className="badge bg-info w-100">⏱️ {workout.duration} min</span>
                    </div>
                    {workout.calories_estimate && (
                      <div className="col-6">
                        <span className="badge bg-danger w-100">🔥 {workout.calories_estimate} cal</span>
                      </div>
                    )}
                  </div>
                </div>
              </div>
            </div>
          ))
        ) : (
          <div className="col-12">
            <p className="text-center">No workouts found</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default Workouts;
