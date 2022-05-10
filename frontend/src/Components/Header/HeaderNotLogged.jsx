import React from "react";
import {NavBarNotLogged} from "../NavBar";
import './Header.css'


function HeaderNotLogged () {
    return(
        <section className="header">
          <section className="header-top">
              <section className='header-top__logo'>
                <a href="/" className="header-logo"> Harmonogram </a>
              </section>
              <section className="header-top__navbar">
                  <section className="header-top__navigation">
                      <NavBarNotLogged/>
                  </section>
                  <hr className="header-top__seperator" />
              </section>
          </section>


        </section>
    )
}

export default HeaderNotLogged