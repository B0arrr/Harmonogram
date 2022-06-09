import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {BrowserRouter as Router, Route, Routes} from "react-router-dom";
import LoggedPage from "./Pages/LoggedPage";
import RegistrationPage from "./Pages/RegistrationPage";
import ManageEmployees from "./Pages/ManageEmployees";
import ManageSchedule from "./Pages/ManageSchedule";
import {UserProvider} from "./Components/TestLogin/UserContext";


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
        <Router>
            <Routes>
                <Route path="/" element={<UserProvider><App/></UserProvider>}/>
                <Route path="/src/Pages/RegistrationPage" element={<RegistrationPage/>}/>
                <Route path="/src/Pages/LoggedPage" element={<LoggedPage/>}/>
                <Route path="/src/Pages/ManageEmployees" element={<ManageEmployees/>}/>
                <Route path="/src/Pages/ManageSchedule" element={<ManageSchedule/>}/>
            </Routes>
        </Router>
    </React.StrictMode>
);


reportWebVitals();
