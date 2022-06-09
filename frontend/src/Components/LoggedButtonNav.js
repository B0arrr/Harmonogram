import React from "react";
import './Style/LoggedButtonNav.css';
import {useNavigate} from 'react-router-dom';

function LoggedButtonNav() {

    const navigate = useNavigate();

    const navigateToMenageEmployees =() => {
        navigate('/src/Pages/ManageEmployees')
    }
    const navigateToMenageSchedule =() => {
        navigate('/src/Pages/ManageEmployees')
    }

        return (
        <div className="containerForLoggedNavBtn">
            <button id="btnMenageEmployees" className="btn btn-primary col-sm-6" onClick={navigateToMenageEmployees}>Menage employees</button>
            <button id="btnMenageSchedule" className="btn btn-primary col-sm-6" onClick={navigateToMenageSchedule}>Menage schedule</button>
        </div>
    );
}

export default LoggedButtonNav;