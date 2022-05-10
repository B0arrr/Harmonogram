import React from "react";
import './NavBar.css'
import {Link} from "react-router-dom";

function NavBarRegister (){
    return (
        <section className="navbar">
                <Link className="navbar-item" to="/"> Home </Link>
                <Link className="navbar-item" to='/'> Log In</Link>
        </section>
    )
}

export default NavBarRegister