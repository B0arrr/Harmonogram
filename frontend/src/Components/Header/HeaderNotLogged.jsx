import React from "react";

import '../Style/Header.css';


function HeaderNotLogged() {
    return (
        <div className="header">
            <a href="/" className="logo">Harmonogram</a>
            <div className="header-right">
                <a href="/">Home</a>
                <a href="/src/Pages/LogIn">Log In</a>
                <a href="/src/Pages/RegistrationPage">Register</a>
            </div>
        </div>
    );
}

export default HeaderNotLogged;