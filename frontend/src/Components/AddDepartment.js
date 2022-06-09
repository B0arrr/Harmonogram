import React from "react";
import '../Components/Style/AddDepartment.css'

function AddDepartment(){

    return(

            <div className="containerForAddDepartment">
                <h1 className="addDepartmentHeader">Add Department: </h1>
                <form className="form formAddDepartment">
                    <input placeholder="Name" className="form-control" type="text" />
                </form>
                <button className="btn btn-primary btnAddDepartment"> Add Department</button>
            </div>

    )
}
export default AddDepartment