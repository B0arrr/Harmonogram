import React from "react";

import {useEffect, useState} from "react";
import Axios from "axios";
import button from "bootstrap/js/src/button";
import { format } from 'date-fns';



function EmployeeScheduleGenerator(){
    const [data, setData] = useState([])

    const [start, setStart] = useState('')
    const [end, setEnd] = useState('')
    const [employee_per_shift, setEmployee_per_shift] = useState('')
    const [shifts, setShifts] = useState('')

    const [errorMessage, setErrorMessage] = useState("");



    const postData = (e) =>{
        e.preventDefault();
        Axios.post(`http://localhost:8000/api/generate_schedule?start=${start}&end=${end}&employee_per_shift=${employee_per_shift}&shifts=${shifts}`,{
            start,
            end,
            employee_per_shift,
            shifts

        }).then(res => console.log("Posting data",res))
            .catch(err => setErrorMessage(err.response.data.detail))
    }

    const arr = data.map((data,index) =>
    {
        return (
            <tr>
                <td >{data.start}</td>
                <td >{data.end}</td>
                <td >{data.employee_per_shift}</td>
                <td >{data.shifts}</td>
            </tr>
        )
    })

    return(
        <div className='workTableContainer'>
            <div className='containerForBorder'>
                <h1 id='workTableHeader'>Schedule Generator</h1>
                <div className='containerFromWorkTable'>
                    <div className='buttonContainer'>
                        <form className='form'>
                            <input placeholder='Start Date (yyyy-mm-dd)' className='form-control' type='text' value={start} onChange={(e) =>setStart(e.target.value)}/>
                            <input placeholder='End Date (yyyy-mm-dd)' className='form-control' type="text" value={end} onChange={(e) =>setEnd(e.target.value)}/>
                            <input placeholder='employee_per_shift' className='form-control' type="text" value={employee_per_shift} onChange={(e) =>setEmployee_per_shift(e.target.value)}/>
                            <input placeholder='shifts' className='form-control' type="text" value={shifts} onChange={(e) =>setShifts(e.target.value)}/>
                        </form>
                        <button className='btn btn-primary col-sm-6' onClick={postData} > Generate </button>
                    </div>

                </div>
            </div>
        </div>
    )
}

export default EmployeeScheduleGenerator