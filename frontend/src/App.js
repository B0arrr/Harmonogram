import './App.css';
import React, {Component} from 'react';
import {useEffect, useState} from "react";
import {HeaderLogged, HeaderLogIn} from './Components/Header';
import Axios from "axios";



function App() {
    const [data, setData] = useState([])

    const [employment_id, setEmployment_id] = useState('')
    const [name, setName] = useState('')
    const [surname, setSurname] = useState('')
    const [position_id, setPosition_id] = useState('')
    const [email, setEmail] = useState('')
    const [login, setLogin] = useState('')
    const [password, setPassword] = useState('')



    // const [name, setName] = useState()
    // const [pos, setPos] = useState([])
    // useEffect(() => {
    //     fetch("http://localhost:8000/api/get_all_positions")
    //         .then(response => response.json())
    //         .then(json => setPos(json))
    // }, [])
    //
    //
    // useEffect(() => {
    //     const fetchData = async () => {
    //         const data = await (await fetch("http://localhost:8000/api")).json()
    //         setName(data.name)
    //     }
    //     fetchData().then()
    //
    // }, [])
    return (
        <div>
            <HeaderLogIn/>
            <div className='containerForLogin'>
                <br/>
                <h1 className='loginHeader'>Zaloguj się: </h1>
                <form className=' form col-sm-6'>
                    <input placeholder='Name' className='form-control' type="text" value={name} onChange={(e) =>setName(e.target.value)}/>
                    <input placeholder='Surname' className='form-control' type="text" value={surname} onChange={(e) =>setSurname(e.target.value)}/>
                    <input placeholder='E-mail' className='form-control' type="text" value={email} onChange={(e) =>setEmail(e.target.value)}/>
                    <input placeholder='Login' className='form-control' type="text" value={login} onChange={(e) =>setLogin(e.target.value)}/>
                    <input placeholder='Password' className='form-control' type="password" value={password} onChange={(e) =>setPassword(e.target.value)}/>
                    <input placeholder='Employment' className='form-control' type="number" value={employment_id} onChange={(e) =>setEmployment_id(e.target.value)}/>
                    <input placeholder='Position' className='form-control' type="number" value={position_id} onChange={(e) =>setPosition_id(e.target.value)}/>
                    </form>
                <button  className='btn btn-primary col-sm-6' > Sing In </button>
            </div>
        </div>


        // <div className='appContainer'>
        //
        //     <div className="testApp">
        //             {/*<HeaderLogIn/>*/}
        //             {/*<h1 >Cześć, {name}</h1>*/}
        //             {/*<h4> {pos.map((item, i) => (*/}
        //             {/*    <ul key={i}>*/}
        //             {/*        <li> Stanowisko: {item.name} ID: {item.id}</li>*/}
        //             {/*    </ul>*/}
        //             {/*))}*/}
        //             {/*</h4>*/}
        //     </div>
        // </div>
    )
}

export default App;
