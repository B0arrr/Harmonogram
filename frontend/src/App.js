import React from "react";
import { Routes, Route } from "react-router-dom";
import { RequireToken } from "./test/Auth";
import Login from "./test/Login";
import LoggedPage from "./Pages/LoggedPage";
import ManageEmployees from "./Pages/ManageEmployees";
import ManageSchedule from "./Pages/ManageSchedule";
import Registration from "./Components/Registration";
import {HeaderRegistration} from "./Components/Header";
import {HeaderLogin} from "./Components/Header";
import BasicEmployeePage from "./Pages/BasicEmployeePage";
import BasicManageSchedule from "./Pages/BasicManageSchedule";
import ListEmployee from "./Components/ListEmployee";


function App(){



    return(
        <div className ="App">
            <Routes>
                <Route path="/" element = {<Login/>}/>
                <Route path="/src/Pages/LoggedPage" element = {
                   <RequireToken>
                       <LoggedPage/>
                   </RequireToken>
                }/>
                <Route path="/src/Pages/ManageEmployees" element = {
                   <RequireToken>
                       <ManageEmployees/>
                   </RequireToken>
                }/>
                <Route path="/src/Pages/ManageSchedule" element = {
                   <RequireToken>
                       <ManageSchedule/>
                   </RequireToken>
                }/>
                <Route path="/src/Pages/RegistrationPage" element = {
                    <div>
                        <HeaderRegistration/>
                        <Registration/>
                    </div>
                }/>
                <Route path="/src/Pages/BasicEmployeePage" element = {
                    <div>
                        <RequireToken>
                            <BasicEmployeePage/>
                        </RequireToken>
                    </div>
                }/>
                <Route path="/src/Pages/BasicManageSchedule" element = {
                    <div>
                        <RequireToken>
                            <BasicManageSchedule/>
                        </RequireToken>
                    </div>
                }/>
            </Routes>
        </div>
    )
}


export default App;


