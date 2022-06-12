import React from "react";
import HeaderManageEmployees from "../Components/Header/HeaderManageEmployees";
import ListEmployee from "../Components/ListEmployee";
import AddEmployee from "../Components/AddEmployee";
import '../Components/Style/ManageEmployees.css';


function ManageEmployees() {


    return (
        <div>
            <HeaderManageEmployees/>
            <div className="containerForManageEmployees">
                <div className="addManageEmployees">
                        <AddEmployee/>
                </div>
                <div className="listManageEmployees">
                        <ListEmployee/>
                </div>
            </div>
        </div>

    );

}

export default ManageEmployees;