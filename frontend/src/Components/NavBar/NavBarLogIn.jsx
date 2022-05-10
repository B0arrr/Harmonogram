import React from "react";
import './NavBar.css'
import {Link} from "react-router-dom";

function NavBarLogIn(){
    return (
        <section className="navbar">
                <Link className="navbar-item" to="/"> Home </Link>
                <Link className="navbar-item" to='/src/Pages/Register'> Register</Link>
        </section>
    )

}

export default NavBarLogIn