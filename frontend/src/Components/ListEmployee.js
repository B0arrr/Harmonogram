import React from "react";
import {useEffect, useState} from "react";
import Axios from "axios";
import "./ListEmployee.css"
import Logged from "../Pages/Logged";



function ListEmployee(){

    const [data, setData] = useState([])
    const [idForDelete, setIdForDelete] = useState('')


    useEffect(() => {
        fetch("http://localhost:8000/api/get_all_employees")
            .then(response => response.json())
            .then(json => setData(json))
    }, [])

    function deleteEmployee(e){

        console.log(e.target.value)
        fetch(`http://localhost:8000/api/delete_employee/${e.target.value}`, {method:`DELETE`})
            .then(()=>this.setState({status:`Delete`}))
    }



    return(
    <div className='listEmployeesContainer'>
            <h1 id='listEmployeesHeader'> Employees List:</h1>
            {/*<div className='buttonContainer'>*/}
            {/*    <input type="number" value={idForDelete} onChange={(e) =>setIdForDelete(e.target.value)}/>*/}
            {/*    <button onClick={()=>deleteOperation(data.id)} className='btnAdd'> Remove employee</button>*/}
            {/*</div>*/}
            <div className='containerFromEmployees'>
                <h4> {data.map((item, i) => (
                    <ul key={i}>
                        <li>
                            Imię: {item.name} <br/>
                            Nazwisko: {item.username}<br/>
                            ID: {item.id} <br/>
                            Email: {item.email} <br/>
                            <button className=' btnDeleteEmployee' value={item.id} onClick={deleteEmployee}>  Delete </button>
                        </li>
                    </ul>
                ))}
                </h4>
            </div>
    </div>
 )
}

export default ListEmployee