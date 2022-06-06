import React from "react";
import {HeaderLogged} from "../Components/Header";
import AddEmployee from "../Components/AddEmployee";
import ListEmployee from "../Components/ListEmployee";
import EmployeeTable from "../Components/EmployeeTable";
import '../Components/Logged.css'


function Logged() {


    return(
        <div className="LogIn">
            <div>
                <HeaderLogged/>
            </div>
            <div className="schedule" >
                <AddEmployee/>
                <ListEmployee/>
                <EmployeeTable/>
            </div>
        </div>
    )
}

export default Logged