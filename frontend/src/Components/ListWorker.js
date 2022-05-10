import React from "react";
import {useEffect, useState} from "react";
import Axios from "axios";
import "./ListWorker.css"
import Logged from "../Pages/Logged";

function listWorker(){

    return(
    <div className='listWorkerContainer'>
        <div className='containerForBorder'>
            <h1 id='listWorkerHeader'> Worker List</h1>
            <div className='buttonContainer'>
                <button className='btnAdd'> Remove employee</button>
                <button className='btnClear'> Clear List</button>
            </div>
            <div className='containerFromWorkers'>

            </div>
        </div>
    </div>
 )
}

export default listWorker