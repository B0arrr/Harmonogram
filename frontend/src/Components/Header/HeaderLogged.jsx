import React from "react";

import '../Style/Header.css';


function HeaderLogged() {
    return (

        <div className="header">
            <a href="/src/Pages/LoggedPage" className="logo">Harmonogram</a>
            <div className="header-right">
                <a href="/src/Pages/LoggedPage">Home</a>
                <a href="/">Log Out</a>
            </div>
        </div>


    );
}

export default HeaderLogged;