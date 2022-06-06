import React from "react";
import {useEffect, useState} from "react";
import Axios from "axios";
import "./AddEmployee.css";
import {HeaderRegister} from "./Header";


function AddEmployee() {
    const [data, setData] = useState([]);


    const [name, setName] = useState('');
    const [surname, setSurname] = useState('');
    const [email, setEmail] = useState('');
    const [employment_id, setEmployment_id] = useState('');
    const [position_id, setPosition_id] = useState('');
    const [login, setLogin] = useState('');
    const [password, setPassword] = useState('');


    const [errorMessage, setErrorMessage] = useState("");

    const resetInputField = () => {
        setName("");
        setSurname("");
        setEmail("");
        setEmployment_id("");
        setPosition_id("");
        setLogin("");
        setPassword("");
    };

    useEffect(() => {
        Axios.get(`http://localhost:8000/api/get_employee_by_login/${employment_id}`)
            .then(res => {
                console.log("Getting from :::", res.data);
                setData(res.data);
            }).catch(err => console.log(err));
    }, []);

    const postData = () => {

        Axios.post(`http://localhost:8000/api/create_employee`, {
            name,
            surname,
            email,
            employment_id,
            position_id,
            login,
            password
        }).then(res => alert(`Employee account created`))
            .then(res => resetInputField())
            .catch(err => setErrorMessage(err.response.data.detail));
    };

    const arr = data.map((data, index) => {
        return (
            <tr>
                <td >{data.name}</td>
                <td >{data.surname}</td>
                <td >{data.email}</td>
                <td >{data.employment_id}</td>
                <td >{data.position_id}</td>
                <td >{data.login}</td>
                <td >{data.password}</td>
            </tr>
        );
    });



    return (
        <div>
            <div className='containerForAddEmployee'>
                <h1 className='addEmployeeHeader'>Add Employee: </h1>
                <h2>{errorMessage}</h2>
                <form className='form'>
                    <input placeholder='Name' className='form-control' type="text" value={name} onChange={(e) =>setName(e.target.value)}/>
                    <input placeholder='Surname' className='form-control' type="text" value={surname} onChange={(e) =>setSurname(e.target.value)}/>
                    <input placeholder='E-mail' className='form-control' type="text" value={email} onChange={(e) =>setEmail(e.target.value)}/>
                    <input placeholder='Login' className='form-control' type="text" value={login} onChange={(e) =>setLogin(e.target.value)}/>
                    <input placeholder='Password' className='form-control' type="password" value={password} onChange={(e) =>setPassword(e.target.value)}/>
                    <input placeholder='Employment' className='form-control' type="number" value={employment_id} onChange={(e) =>setEmployment_id(e.target.value)}/>
                    <input placeholder='Position' className='form-control' type="number" value={position_id} onChange={(e) =>setPosition_id(e.target.value)}/>
                </form>
                <button  className='btn btn-primary btnAddEmployee' onClick={postData}> Register </button>
            </div>
        </div>
    );
}

export default AddEmployee;