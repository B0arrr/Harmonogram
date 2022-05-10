import React from "react";
import './NavBar.css'
import {Link} from "react-router-dom";

function NavBarLogged (){
    return (
        <section className="navbar">
                <Link className="navbar-item" to="/src/Pages/Logged"> Home </Link>
                <Link className="navbar-item" to="/src/Pages/MyProfile"> My Profile</Link>
                <Link className="navbar-item" to="/"> Log Out</Link>
        </section>
    )

}
export default NavBarLogged