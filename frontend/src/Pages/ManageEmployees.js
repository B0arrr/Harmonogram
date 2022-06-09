import React from "react";
import HeaderManageEmployees from "../Components/Header/HeaderManageEmployees";
import ListEmployee from "../Components/ListEmployee";
import ListDepartment from "../Components/ListDepartment";
import AddEmployee from "../Components/AddEmployee";
import AddDepartment from "../Components/AddDepartment";
import '../Components/Style/ManageEmployees.css';

function ManageEmployees() {


    return (
        <div>
            <HeaderManageEmployees/>
            <div className="containerForManageEmployees">
                <div className="addManageEmployees">
                        <AddDepartment/>
                    <br/>
                        <AddEmployee/>
                </div>
                <div className="listManageEmployees">
                        <ListDepartment/>
                    <br/>
                        <ListEmployee/>
                </div>
            </div>
        </div>

    );

}

export default ManageEmployees;