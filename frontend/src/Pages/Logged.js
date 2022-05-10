import React from "react";
import {HeaderLogged} from "../Components/Header";
import AddWorker from "../Components/AddWorker";
import ListWorker from "../Components/ListWorker";
import TimeTable from "../Components/WorkTable";
import '../Components/Logged.css'


function Logged() {


    return(
        <div className="LogIn">
            <div>
                <HeaderLogged/>
            </div>
            <div className="harmonogram" >
                <AddWorker/>
                <ListWorker/>
                <TimeTable/>
            </div>
        </div>
    )
}

export default Logged