import React from "react";
import {NavBarLogged} from "../NavBar";
import './Header.css'


function HeaderLogged () {
    return(
        <section className="header">
            <section className="header-top">
                <section className='header-top__logo'>
                    <a href="/src/Pages/Logged" className="header-logo"> Harmonogram </a>
                </section>
                <section className="header-top__navbar">
                    <section className="header-top__navigation">
                        <NavBarLogged/>
                    </section>
                    <hr className="header-top__seperator" />
                </section>
            </section>
            <section className="header-bottom">
                <section className="header-bottom__position">
                    Kierownik
                </section>
                <section className="header-bottom__email">
                    maciek@gmail.com
                </section>
            </section>
        </section>
    )
}

export default HeaderLogged