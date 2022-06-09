import React, {useEffect, useState} from "react";
import "./Style/ListEmployee.css";


function ListEmployee() {

    const [data, setData] = useState([]);
    const [status, setStatus] = useState('')
    const [idForDelete, setIdForDelete] = useState('');
    const [employment, setEmployment] = useState([]);


    useEffect(() => {
        fetch("http://localhost:8000/api/get_all_employees")
            .then(response => response.json())
            .then(json => setData(json));

    }, []);

    useEffect(() => {
        fetch(`http://localhost:8000/api/get_employment_by_id/1`)
            .then(res => res.json())
            .then(json => setEmployment(json));

    }, []);

    function deleteEmployee(e) {
        console.log(e.target.value);
        e.target.style.backgroundColor = 'red'
        e.target.innerHTML = 'Employee deleted'
        fetch(`http:/localhost:8000/api/delete_employee/${e.target.value}`, {method: `DELETE`})
            .then(() => setStatus('Deleted'));
    }



    return (
        <div className="listEmployeesContainer">
            <h1 className="listEmployeesHeader"> Employees List:</h1>
            <div className="containerForEmployees">
                <h4 className="listEmployeesH4"> {data.map((item, i) => (
                    <ul className="listEmployeesUl" key={i}>
                        <li className="listEmployeesLi">
                            Imię: {item.name} <br/>
                            Nazwisko: {item.surname}<br/>
                            ID: {item.id} <br/>
                            Email: {item.email} <br/>
                            Etat: {item.employment_id} <br/>
                        </li>
                        <button className=' btnDeleteEmployee' value={item.id} onClick={deleteEmployee}>  Delete employee </button>
                    </ul>
                ))}
                </h4>
            </div>
        </div>
    );
}

export default ListEmployee;