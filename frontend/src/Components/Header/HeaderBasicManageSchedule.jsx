import React from "react";
import '../Style/Header.css';
import {useNavigate} from "react-router";


function HeaderBasicManageSchedule() {
    const navigate = useNavigate();
    const signOut = () => {
        localStorage.removeItem('idEmployee')
        localStorage.removeItem("temitope");
        navigate("/");
    };
    return (
        <div className="header">
            <a href="/src/Pages/BasicEmployeePage" className="logo">Harmonogram</a>
            <div className="header-right">
                <a href="/src/Pages/BasicEmployeePage">Management Panel</a>
                <a onClick={signOut} href="/">Sing Out</a>
            </div>
        </div>
    );
}


export default HeaderBasicManageSchedule;