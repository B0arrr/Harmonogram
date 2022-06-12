import React from "react";
import './Style/BasicButtonNav.css';
import {useNavigate} from 'react-router-dom';

function BasicLoggedButtonNav() {

    const navigate = useNavigate();

    const navigateToMenageSchedule = () => {
        navigate('/src/Pages/BasicManageSchedule');
    };

    return (
        <div className="containerForLoggedNavBtn">
            <button id="btnMenageSchedule" className="btn btn-primary col-sm-6"
                    onClick={navigateToMenageSchedule}>Menage schedule
            </button>
        </div>
    );
}


export default BasicLoggedButtonNav;