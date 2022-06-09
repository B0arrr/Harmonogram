import '../Components/Style/Login.css';
import React, {useState} from 'react';


function Login() {
    const [data, setData] = useState([]);

    const [employment_id, setEmployment_id] = useState('');
    const [name, setName] = useState('');
    const [surname, setSurname] = useState('');
    const [position_id, setPosition_id] = useState('');
    const [email, setEmail] = useState('');
    const [login, setLogin] = useState('');
    const [password, setPassword] = useState('');

    return (
        <div>

            <div className="containerForLogin">
                <br/>
                <h1 className="loginHeader">Zaloguj się: </h1>
                <form className=" form col-sm-6">
                    <input placeholder="Name" className="form-control" type="text" value={name}
                           onChange={(e) => setName(e.target.value)}/>
                    <input placeholder="Surname" className="form-control" type="text" value={surname}
                           onChange={(e) => setSurname(e.target.value)}/>
                    <input placeholder="E-mail" className="form-control" type="text" value={email}
                           onChange={(e) => setEmail(e.target.value)}/>
                    <input placeholder="Login" className="form-control" type="text" value={login}
                           onChange={(e) => setLogin(e.target.value)}/>
                    <input placeholder="Password" className="form-control" type="password" value={password}
                           onChange={(e) => setPassword(e.target.value)}/>
                    <input placeholder="Employment" className="form-control" type="number" value={employment_id}
                           onChange={(e) => setEmployment_id(e.target.value)}/>
                    <input placeholder="Position" className="form-control" type="number" value={position_id}
                           onChange={(e) => setPosition_id(e.target.value)}/>
                </form>
                <button className="btn btn-primary col-sm-6"> Sing In</button>
            </div>
        </div>


    );
}

export default Login;
