import React from "react";
import './NavBar.css'
import {Link} from "react-router-dom";

function NavBarNotLogged (){
    return (
        <section className="navbar">
                <Link className="navbar-item" to="/"> Home </Link>
                <Link className="navbar-item" to='/src/Pages/LogIn'> Log In</Link>
                <Link className="navbar-item" to='/src/Pages/Register'> Register</Link>
        </section>
    )

}
export default NavBarNotLogged