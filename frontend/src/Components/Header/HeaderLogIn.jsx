import React from "react";
import './Header.css'



function HeaderLogIn() {
    return (
        <div className="header">
            <a href="/" className="logo">Harmonogram</a>
            <div className="header-right">
                <a href="/">Home</a>
                <a href="/src/Pages/Register">Register</a>
            </div>
        </div>
    )
}
export default HeaderLogIn


