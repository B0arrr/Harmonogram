import './App.css';
import React, {Component} from 'react';
import {useEffect, useState} from "react";
import {HeaderLogIn} from './Components/Header';
import Axios from "axios";


function App() {
    const [name, setName] = useState()
    const [pos, setPos] = useState([])
    useEffect(() => {
        fetch("http://localhost:8000/api/get_all_positions")
            .then(response => response.json())
            .then(json => setPos(json))
    }, [])


    useEffect(() => {
        const fetchData = async () => {
            const data = await (await fetch("http://localhost:8000/api")).json()
            setName(data.name)
        }
        fetchData().then()

    }, [])

    return (
        <div className="App">
            <div >
                <HeaderLogIn/>
                <h1 >Cześć, {name}</h1>
                <h4> {pos.map((item, i) => (
                    <ul key={i}>
                        <li> Stanowisko: {item.name} ID: {item.id}</li>
                    </ul>
                ))}
                </h4>
            </div>
        </div>
    )
}

export default App;
