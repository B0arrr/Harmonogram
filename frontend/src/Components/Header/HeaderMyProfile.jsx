import React from "react";
import { NavBarMyProfile} from "../NavBar";
import './Header.css'


function HeaderMyProfile () {
    return(
        <section className="header">
            <section className="header-top">
                <section className='header-top__logo'>
                    <a href="/src/Pages/Logged" className="header-logo"> Harmonogram </a>
                </section>
                <section className="header-top__navbar">
                    <section className="header-top__navigation">
                        <NavBarMyProfile/>
                    </section>
                    <hr className="header-top__seperator" />
                </section>
            </section>
        </section>
    )
}

export default HeaderMyProfile