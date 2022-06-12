import React, {useState} from "react";
import './Style/EmployeeScheduleGenerator.css';
import Axios from "axios";
import button from "bootstrap/js/src/button";


function EmployeeScheduleGenerator() {
    const [data, setData] = useState([]);

    const [start, setStart] = useState('');
    const [end, setEnd] = useState('');
    const [employee_per_shift, setEmployee_per_shift] = useState('');
    const [shifts, setShifts] = useState('');

    const [errorMessage, setErrorMessage] = useState("");


    const postData = (e) => {
        e.preventDefault();
        Axios.post(`http://127.0.0.1:8000/api/generate_schedule?start=${start}&end=${end}&employee_per_shift=${employee_per_shift}&shifts=${shifts}&department=${department}`, {
            start,
            end,
            employee_per_shift,
            shifts,
            department

        }).then(res => alert(`Schedule generated`))
            .then(res => console.log("Posting data", res))
            .catch(err => setErrorMessage(err.response.data.detail));
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
    return (
        <div className="employeeScheduleGeneratorContainer">
            <h1 className="employeeScheduleGeneratorHeader">Schedule Generator: </h1>

            <form className="form">
                <input placeholder="Start Date (yyyy-mm-dd)" className="form-control" type="text"
                       value={start} onChange={(e) => setStart(e.target.value)}/>
                <input placeholder="End Date (yyyy-mm-dd)" className="form-control" type="text" value={end}
                       onChange={(e) => setEnd(e.target.value)}/>
                <input placeholder="Employee per shift" className="form-control" type="number"
                       value={employee_per_shift} onChange={(e) => setEmployee_per_shift(e.target.value)}/>
                <input placeholder="Shifts" className="form-control" type="number" value={shifts}
                       onChange={(e) => setShifts(e.target.value)}/>

                <select className="form-select selectPosition" aria-label="Default select example"
                        value={department} onChange={chooseDepartment}>
                    {optionsDepartments.map(option2 => (
                        <option key={option2.value} value={option2.text}>
                            {option2.text}
                        </option>
                    ))}
                </select>

            </form>
            <button className="btn btn-primary col-sm-6 btnEmployeeScheduleGenerator" onClick={postData}> Generate
            </button>

        </div>

    );
}


export default EmployeeScheduleGenerator;