
import React from "react";
import HeaderManageSchedule from "../Components/Header/HeaderManageSchedule";
import SchedulePicker from "../Components/SchedulePicker";
import EmployeeScheduleGenerator from "../Components/EmployeeScheduleGenerator";
import Schedule from "../Components/Schedule";
import'../Components/Style/ManageSchedule.css'

function ManageSchedule() {
    return (
        <div>
            <HeaderManageSchedule/>
            <div className='containerForManageSchedule'>
                <div className='employeeScheduleGenAndPick'>
                    <EmployeeScheduleGenerator/>
                    <br/>
                    <SchedulePicker/>
                </div>
                <div className='employeeSchedule'>
                    <Schedule/>
                </div>
            </div>
        </div>
    );
}


export default ManageSchedule;