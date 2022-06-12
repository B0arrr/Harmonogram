import { useNavigate } from "react-router";
import { fetchToken, setToken } from "./Auth";
import { useState } from "react";
import axios from "axios";
import '../Components/Style/Login.css';
import {HeaderLogin} from "../Components/Header";
import {data} from "autoprefixer";
import Axios from "axios";

export default function Login() {
    const navigate = useNavigate();
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const  [data, setData] = useState([])
    const [emailEmployee, setEmailEmployee] = useState('')






    //check to see if the fields are not empty
    const login = () => {
        if ((username === "") && (password === "")) {
            alert('Wrong password or email')
            return;
        } else {
            // make api call to our backend. we'll leave thisfor later
            const params = new URLSearchParams();
            params.append('username', username);
            params.append('password', password);



            axios.post("http://localhost:8000/api/login/access-token", params)
                .then(function (response) {
                    if (response.data.access_token) {
                        setToken(response.data.access_token);

                        Axios.get(`http://localhost:8000/api/get_employee_by_email/${username}`)
                            .then(res => {
                                console.log(res.data)
                                setData(res.data)
                                if (res.data.position_id == 1){
                                    localStorage.setItem("inputEmailValue", username);
                                    navigate("/src/Pages/LoggedPage");
                                }else {
                                    localStorage.setItem("inputEmailValue", username);
                                    navigate("/src/Pages/BasicEmployeePage");
                                }
                            })
                            .catch((error) =>{
                                console.log(error);
                            })

                    }
                })
        }
    }





    return (
        <div>
            <HeaderLogin/>
            <div>
                {fetchToken() ? (
                    <p>you are logged in</p>
                ) : (
                    <div className='containerForLogin'>
                    <h1 className="loginHeader" >Zaloguj się: </h1>
                        <form className='form col-sm-6'>
                            <input className='form-control' placeholder='E-mail' type="text"onChange={(e) => setUsername(e.target.value)}/>
                            <input className='form-control' placeholder='Password' type="password" onChange={(e) => setPassword(e.target.value)}/>
                            <button className='btn btn-primary buttonSingIn' type="button" onClick={login}>Login</button>
                        </form>
                    </div>
                )}
            </div>
        </div>
    );
}

