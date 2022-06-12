import React, {useState} from "react";
import './Style/SchedulePickerForEmployee.css';
import button from "bootstrap/js/src/button";
import {useEffect} from "react";
import Axios from "axios";


function SchedulePickerForEmployee() {



    useEffect(() => {
        Axios.get(`http://localhost:8000/api/get_employee_by_email/${localStorage.getItem('inputEmailValue')}`)
            .then(res => {
                console.log("Gettin", res.data.id);
                setID(res.data.id);

            }).catch(err => console.log(err));
    }, []);

    const [startValue, setStartValue] = useState('');
    const [endValue, setEndValue] = useState('');
    const [id, setID] = useState('');

    const handleChange = (e) => {
        setStartValue(e.target.value);
        localStorage.setItem("inputValue", e.target.value);
        localStorage.setItem("idEmployee", id);
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

export default SchedulePickerForEmployee;