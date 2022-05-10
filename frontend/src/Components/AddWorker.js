import React from "react";
import {useEffect, useState} from "react";
import Axios from "axios";
import "./AddWorker.css"


function AddWorker(){
    const [data, setData] = useState([])

    const [name, setName] = useState('')
    const [surname, setSurname] = useState('')
    const [email, setEmail] = useState('')
    const [employment_id, setEployment_id] = useState('')
    const [position_id, setPosition_id] = useState('')

    useEffect(() =>{
        Axios.get(`http://localhost:8000/api/get_employee_by_login/${employment_id}`)
            .then(res => {
                console.log("Getting from :::",res.data)
                setData(res.data)
            }).catch(err =>console.log(err))
    },[])
    const postData = (e) =>{
        e.preventDefault();
        Axios.post(`http://localhost:8000/api/create_employee`,{
            name,
            surname,
            email,
            employment_id,
            position_id
        }).then(res => console.log("Posting data",res)).catch(err =>console.log(err))
    }

    const arr = data.map((data,index) =>
    {
        return (
            <tr>
                <td style={{border: '1px solid black'}}>{data.id}</td>
                <td style={{border: '1px solid black'}}>{data.name}</td>
                <td style={{border: '1px solid black'}}>{data.surname}</td>
                <td style={{border: '1px solid black'}}>{data.email}</td>
                <td style={{border: '1px solid black'}}>{data.employment_id}</td>
                <td style={{border: '1px solid black'}}>{data.position_id}</td>
            </tr>
        )
    })

    return(
        <div className="addWorkerContainer">
            <div className='containerForBorder'>
                <h1 id='addWorkerHeader'>Add Worker: </h1>
                <br/>
                <form>
                    <label> Name: </label>
                    <input type="text" value={name} onChange={(e) =>setName(e.target.value)}/>
                    <hr/>

                    <label> Surname: </label>
                    <input type="text" value={surname} onChange={(e) =>setSurname(e.target.value)}/>
                    <hr/>

                    <label>E-mail: </label>
                    <input type="text" value={email} onChange={(e) =>setEmail(e.target.value)}/>
                    <hr/>

                    <label>Employment ID: </label>
                    <input type="number" value={employment_id} onChange={(e) =>setEployment_id(e.target.value)}/>
                    <hr/>

                    <label>Position ID: </label>
                    <input type="number" value={position_id} onChange={(e) =>setPosition_id(e.target.value)}/>
                </form>
                <br/>
                <button className="AddWorkerButton" onClick={postData}> Add employee </button>
                <br/>
            </div>
        </div>
    )
}
export default AddWorker