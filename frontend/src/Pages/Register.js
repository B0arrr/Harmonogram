import React from "react";
import {useEffect, useState} from "react";
import Axios from "axios";
import "./Register.css"
import {HeaderRegister} from "../Components/Header";
import axios from "axios";

function Register(){
    const [data, setData] = useState([])

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
        Axios.put(`http://localhost:8000/api/create_employee`,{
            email,
            login,
            password
        }).then(res => console.log("Posting data",res)).catch(err =>console.log(err))
    }


    // TESTOWA
    // function updatePost() {
    //     axios
    //         .put(`http://localhost:8000/api/create_account/{email}`,{
    //             login: '',
    //             password: ''
    //         })
    //         .then((response) => {
    //         setData(response.data)
    //     })
    // }



    const arr = data.map((data,index) =>
    {
        return (
            <tr>
                <td style={{border: '1px solid black'}}>{data.email}</td>
                <td style={{border: '1px solid black'}}>{data.login}</td>
                <td style={{border: '1px solid black'}}>{data.password}</td>
            </tr>
        )
    })

    return(
        <div >
            <HeaderRegister/>
            <div className="registerContainer">
                <h1 id='registerHeader'>Zarejestruj się: </h1>
                <br/>
                <form>
                    <label>E-mail: </label>
                    <input type="text" value={email} onChange={(e) =>setEmail(e.target.value)}/>
                    <hr/>

                    <label>Login: </label>
                    <input type="text" value={login} onChange={(e) =>setLogin(e.target.value)}/>
                    <hr/>

                    <label>Password: </label>
                    <input type="password" value={password} onChange={(e) =>setPassword(e.target.value)}/>
                </form>
                </div>
            <button className="registerBTN" onClick={postData}> Register </button>
        </div>
    )
}
export default Register