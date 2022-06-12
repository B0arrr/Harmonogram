import React from "react";
import SchedulePickerForEmployee from "../Components/SchedulePickerForEmployee";
import Schedule from "../Components/Schedule";
import'../Components/Style/SchedulePickerForEmployee.css'
import HeaderBasicManageSchedule from "../Components/Header/HeaderBasicManageSchedule";
import BasicSchedule from "../Components/BasicSchedule";

function BasicManageSchedule() {
    return (
        <div>
            <HeaderBasicManageSchedule/>
            <div className='containerForBasicManageSchedule'>
                <div className='employeeSchedulePicker'>
                    <SchedulePickerForEmployee/>
                </div>
            </div>
            <div className='employeeSchedule'>
                <BasicSchedule/>
            </div>


        </div>
    );
}


export default BasicManageSchedule;