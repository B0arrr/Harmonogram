import React from "react";
import {HeaderLogged} from "../Components/Header";
import AddEmployee from "../Components/AddEmployee";
import ListEmployee from "../Components/ListEmployee";
import EmployeeScheduleGenerator from "../Components/EmployeeScheduleGenerator";
import '../Components/Logged.css'
import EmployeeSchedule from "../Components/EmployeeSchedule";


function Logged() {


    return(
        <div className="LogIn">
            <div>
                <HeaderLogged/>
            </div>
            <div className="schedule" >

                <AddEmployee/>
                <EmployeeScheduleGenerator/>
                <ListEmployee/>
                <EmployeeSchedule/>

            </div>
        </div>
    )
}

export default Logged