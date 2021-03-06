import React from "react";
import '../Style/Header.css';
import {useNavigate} from "react-router";


function HeaderManageSchedule() {
    const navigate = useNavigate();
    const signOut = () => {
        localStorage.removeItem('idEmployee')
        localStorage.removeItem("temitope");
        navigate("/");
    };
    return (
        <div className="header">
            <a href="/src/Pages/LoggedPage" className="logo">Harmonogram</a>
            <div className="header-right">
                <a href="/src/Pages/LoggedPage">Management Panel</a>
                <a href="/src/Pages/ManageEmployees"> Manage Employees</a>
                <a onClick={signOut} href="/">Sing Out</a>
            </div>
        </div>
    );
}


export default HeaderManageSchedule;