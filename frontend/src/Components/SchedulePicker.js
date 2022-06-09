import React, {useEffect, useState} from "react";
import Axios from "axios";
import './Style/SchedulePicker.css';
import button from "bootstrap/js/src/button";


function SchedulePicker() {

    const [startValue, setStartValue] = useState('');
    const [endValue, setEndValue] = useState('');

    const handleChange = (e) => {
        setStartValue(e.target.value);
        localStorage.setItem("inputValue", e.target.value);
    };

    const handleChange2 = (e) => {
        setEndValue(e.target.value);
        localStorage.setItem("inputValue2", e.target.value);
    };


    const aa = () => {
        window.location.reload();
    };

    console.log(startValue);
    return (

        <div className="schedulePickerContainer">
            <h1 className="schedulePickerHeader">Schedule:</h1>
                <form className="form">
                    <input placeholder="Start Date (yyyy-mm-dd)" className="aaa form-control " type="text"
                           value={startValue} onChange={handleChange}/>
                    <input placeholder="End Date (yyyy-mm-dd)" className=" form-control" type="text" value={endValue}
                           onChange={handleChange2}/>
                    <button className=" scheduleBtn btn btn-primary schedulePickerBtn" onClick={aa}> Show Schedule</button>
                </form>
        </div>
    );
}

export default SchedulePicker;