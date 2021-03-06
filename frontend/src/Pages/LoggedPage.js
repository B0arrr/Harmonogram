import { useNavigate } from "react-router";
import React from "react";
import {RequireToken} from "../test/Auth";
import HeaderLogged from "../Components/Header/HeaderLogged";
import UserProfileCard from "../Components/UserProfileCard";
import LoggedButtonNav from "../Components/LoggedButtonNav";
import '../Components/Style/LoggedPage.css';


function LoggedPage() {

    return (
        <div className="LogIn">
            <div>
                <HeaderLogged/>
            </div>
            <div className="schedule">
                <UserProfileCard/>
                <LoggedButtonNav/>

            </div>
        </div>
    );
}

export default LoggedPage;