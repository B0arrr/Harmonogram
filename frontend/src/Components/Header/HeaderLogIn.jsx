import React from "react";
import './Header.css'
import {NavBarLogIn} from "../NavBar";


function HeaderLogIn() {
    return (
        <section className="header">
            <section className="header-top">
                <section className='header-top__logo'>
                    <a href="/" className="header-logo"> Harmonogram </a>
                </section>
                <section className="header-top__navbar">
                    <section className="header-top__navigation">
                        <NavBarLogIn/>
                    </section>
                    <hr className="header-top__seperator"/>
                </section>
            </section>
            <section className="header-bottom">
            </section>
        </section>
    )
}
export default HeaderLogIn


