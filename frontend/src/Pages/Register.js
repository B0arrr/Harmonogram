import React from "react";
import {useEffect, useState} from "react";
import Axios from "axios";
import "./Register.css"
import {HeaderRegister} from "../Components/Header";
import {Link} from "react-router-dom";
import button from "bootstrap/js/src/button";


function Register(){
    const [data, setData] = useState([])
    const [errorMessage, setErrorMessage] = useState("");

    const [employment_id, setEmployment_id] = useState('')
    const [name, setName] = useState('')
    const [surname, setSurname] = useState('')
    const [position_id, setPosition_id] = useState('')
    const [email, setEmail] = useState('')
    const [login, setLogin] = useState('')
    const [password, setPassword] = useState('')


    useEffect(() =>{
        Axios.get(`http://localhost:8000/api/get_employee_by_login/${login}`)
            .then(res => {
                console.log("Getting from :::",res.data)
                setData(res.data)
            }).catch(err =>console.log(err))
    },[])
    const postData = (e) =>{
        e.preventDefault();
        Axios.post(`http://localhost:8000/api/create_employee`,{
            email,
            login,
            password,
            employment_id,
            name,
            surname,
            position_id
        }).then(res =>alert(`Account created ${window.location.href='/'}`))
            .catch(err => setErrorMessage(err.response.data.detail))
    }


    const arr = data.map((data,index) =>
    {
        return (
            <tr>
                <td style={{border: '1px solid black'}}>{data.email}</td>
                <td style={{border: '1px solid black'}}>{data.login}</td>
                <td style={{border: '1px solid black'}}>{data.password}</td>
                <td style={{border: '1px solid black'}}>{data.name}</td>
                <td style={{border: '1px solid black'}}>{data.surname}</td>
                <td style={{border: '1px solid black'}}>{data.employment_id}</td>
                <td style={{border: '1px solid black'}}>{data.position_id}</td>
            </tr>
        )
    })



    return(
        <div>
            <HeaderRegister/>
            <div className='containerForRegister'>
                <br/>
                <h1 className='registerHeader'>Zarejestruj się: </h1>
                <h2>{errorMessage}</h2>
                <form className='form col-sm-6'>
                    <input placeholder='Name' className='form-control' type="text" value={name} onChange={(e) =>setName(e.target.value)}/>
                    <input placeholder='Surname' className='form-control' type="text" value={surname} onChange={(e) =>setSurname(e.target.value)}/>
                    <input placeholder='E-mail' className='form-control' type="text" value={email} onChange={(e) =>setEmail(e.target.value)}/>
                    <input placeholder='Login' className='form-control' type="text" value={login} onChange={(e) =>setLogin(e.target.value)}/>
                    <input placeholder='Password' className='form-control' type="password" value={password} onChange={(e) =>setPassword(e.target.value)}/>
                    <input placeholder='Employment' className='form-control' type="number" value={employment_id} onChange={(e) =>setEmployment_id(e.target.value)}/>
                    <input placeholder='Position' className='form-control' type="number" value={position_id} onChange={(e) =>setPosition_id(e.target.value)}/>
                    </form>
                    <button className='btn btn-primary col-sm-6' onClick={postData} > Register </button>
           </div>
        </div>
    )
}
export default Register