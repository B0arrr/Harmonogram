import React, {useState} from "react";
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

    const handleChange3 = (e) => {
        setDepartment(e.target.value);
        localStorage.setItem("inputValue3", e.target.value);
    };

    const aa = () => {
        window.location.reload();
    };


    const optionsDepartments = [
        {value: '', text: 'Choose department'},
        {value: '1', text: 'Biuro obsługi klienta'},
        {value: '2', text: 'Księgowość'},
        {value: '3', text: 'Logistyka'},
        {value: '4', text: 'Produkcja'},
        {value: '5', text: 'Handlowy'},
        {value: '6', text: 'Marketing'},
        {value: '7', text: 'Magazyn'},
        {value: '8', text: 'HR'},
        {value: '9', text: 'IT'},
    ]
    const [department, setDepartment] = useState(optionsDepartments[0].value);
    const chooseDepartment = event => {
        console.log(event.target.value);
        setDepartment(event.target.value);
    };

    console.log(startValue);
    return (

        <div className="schedulePickerContainer">
            <h1 className="schedulePickerHeader">Schedule Picker:</h1>
            <form className="form">
                <input placeholder="Start Date (yyyy-mm-dd)" className="aaa form-control " type="text"
                       value={startValue} onChange={handleChange}/>
                <input placeholder="End Date (yyyy-mm-dd)" className=" form-control" type="text" value={endValue}
                       onChange={handleChange2}/>

                <select className="form-select selectPosition" aria-label="Default select example"
                        value={department} onChange={chooseDepartment}>
                    {optionsDepartments.map(option2 => (
                        <option key={option2.value} value={option2.text}>
                            {option2.text}
                        </option>
                    ))}
                </select>

                <button className=" scheduleBtn btn btn-primary schedulePickerBtn" onClick={aa}> Show Schedule</button>
            </form>
        </div>
    );
}

export default SchedulePicker;