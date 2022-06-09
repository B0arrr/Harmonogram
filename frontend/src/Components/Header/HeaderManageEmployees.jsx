import React from "react";
import '../Style/Header.css';


function HeaderManageEmployees() {
    return (
        <div className="header">
            <a href="/src/Pages/LoggedPage" className="logo">Harmonogram</a>
            <div className="header-right">
                <a href="/src/Pages/LoggedPage">Management Panel</a>
                <a href='/src/Pages/ManageSchedule'> Manage Schedule</a>
                <a href="/">Log Out</a>
            </div>
        </div>
    );
}

export default HeaderManageEmployees;