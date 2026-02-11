import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link, NavLink } from 'react-router-dom';
import './App.css';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function Home() {
  return (
    <div className="container mt-4">
      <div className="jumbotron">
        <h1 className="display-3">OctoFit Tracker by NOS</h1>
        <p className="lead">Monitorize a sua atividade física, compete com a sua equipa e atinja os seus objetivos de fitness.</p>
        <hr className="my-4" />
        <p>Plataforma profissional de gestão de fitness corporativo</p>
      </div>
      
      <div className="row mt-5">
        <div className="col-md-3 mb-4">
          <div className="card border-primary">
            <div className="card-body text-center">
              <h3 className="card-title" style={{fontSize: '1.1rem'}}>Utilizadores</h3>
              <p className="card-text" style={{fontSize: '0.9rem'}}>Consulte todos os utilizadores registados e os seus perfis</p>
              <Link to="/users" className="btn btn-primary">Ver Utilizadores</Link>
            </div>
          </div>
        </div>
        <div className="col-md-3 mb-4">
          <div className="card border-success">
            <div className="card-body text-center">
              <h3 className="card-title" style={{fontSize: '1.1rem'}}>Equipas</h3>
              <p className="card-text" style={{fontSize: '0.9rem'}}>Explore as equipas e junte-se à competição</p>
              <Link to="/teams" className="btn btn-success">Ver Equipas</Link>
            </div>
          </div>
        </div>
        <div className="col-md-3 mb-4">
          <div className="card border-info">
            <div className="card-body text-center">
              <h3 className="card-title" style={{fontSize: '1.1rem'}}>Atividades</h3>
              <p className="card-text" style={{fontSize: '0.9rem'}}>Registe e acompanhe as suas atividades físicas</p>
              <Link to="/activities" className="btn btn-info">Ver Atividades</Link>
            </div>
          </div>
        </div>
        <div className="col-md-3 mb-4">
          <div className="card border-warning">
            <div className="card-body text-center">
              <h3 className="card-title" style={{fontSize: '1.1rem'}}>Classificação</h3>
              <p className="card-text" style={{fontSize: '0.9rem'}}>Veja quem lidera nos desafios de fitness</p>
              <Link to="/leaderboard" className="btn btn-warning">Ver Classificação</Link>
            </div>
          </div>
        </div>
      </div>
      
      <div className="row mb-4">
        <div className="col-12">
          <div className="card border-danger">
            <div className="card-body text-center">
              <h3 className="card-title">Treinos Personalizados</h3>
              <p className="card-text">Receba sugestões de treino adaptadas ao seu nível</p>
              <Link to="/workouts" className="btn btn-danger">Ver Treinos</Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-dark bg-primary sticky-top">
          <div className="container-fluid">
            <Link className="navbar-brand d-flex align-items-center" to="/">
              <img 
                src="/nos-logo.png" 
                alt="NOS Logo" 
                height="40" 
                className="me-2"
              />
              <span>OctoFit Tracker</span>
            </Link>
            <button 
              className="navbar-toggler" 
              type="button" 
              data-bs-toggle="collapse" 
              data-bs-target="#navbarNav" 
              aria-controls="navbarNav" 
              aria-expanded="false" 
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav ms-auto">
                <li className="nav-item">
                  <NavLink className="nav-link" to="/" end>Início</NavLink>
                </li>
                <li className="nav-item">
                  <NavLink className="nav-link" to="/users">Utilizadores</NavLink>
                </li>
                <li className="nav-item">
                  <NavLink className="nav-link" to="/teams">Equipas</NavLink>
                </li>
                <li className="nav-item">
                  <NavLink className="nav-link" to="/activities">Atividades</NavLink>
                </li>
                <li className="nav-item">
                  <NavLink className="nav-link" to="/leaderboard">Classificação</NavLink>
                </li>
                <li className="nav-item">
                  <NavLink className="nav-link" to="/workouts">Treinos</NavLink>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/users" element={<Users />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/workouts" element={<Workouts />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
