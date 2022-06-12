import React from "react";
import BasicUserProfileCard from "../Components/BasicUserProfileCard";
import BasicLoggedButtonNav from "../Components/BasicLoggedButtonNav";
import HeaderBasicLogged from "../Components/Header/HeaderBasicLogged";

function BasicEmployeePage(){
    return(
        <div>
            <HeaderBasicLogged/>
            <BasicUserProfileCard/>
            <BasicLoggedButtonNav/>
        </div>
    )
}
export default BasicEmployeePage