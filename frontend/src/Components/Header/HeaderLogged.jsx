import React from "react";

import './Header.css'


function HeaderLogged () {
    return(

        <div className="header">
            <a href="/" className="logo">Harmonogram</a>
            <div className="header-right">
                <a href="/src/Pages/Logged">Home</a>
                <a  href="/src/Pages/MyProfile">My Profile</a>
                <a  href="/">Log Out</a>
            </div>
        </div>


    )
}

export default HeaderLogged