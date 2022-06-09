import React, {useEffect, useState} from "react";
import Axios from "axios";
import "./Style/AddEmployee.css";


function AddEmployee() {
    const [data, setData] = useState([]);

    const [name, setName] = useState('');
    const [surname, setSurname] = useState('');
    const [email, setEmail] = useState('');
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

    const optionsEmployment = [
        {value: '', text: 'Choose employment'},
        {value: '1', text: 'Cały etat'},
        {value: '2', text: 'Pół etatu'},
    ];

    const [employment_id, setEmployment_id] = useState(optionsEmployment[0].value);
    const chooseEmployment = event => {
        console.log(event.target.value);
        setEmployment_id(event.target.value);
    };

    const optionsPosition = [
        {value: '', text: 'Choose position'},
        {value: '1', text: 'Kierownik'},
        {value: '2', text: 'Pracownik'},
    ];

    const [position_id, setPosition_id] = useState(optionsPosition[0].value);
    const choosePosition = event => {
        console.log(event.target.value);
        setPosition_id(event.target.value);
    };

    return (
        <div>
            <div className="containerForAddEmployee">
                <h1 className="addEmployeeHeader">Add Employee: </h1>
                <h2>{errorMessage}</h2>
                <form className="form">
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
                    <select className="form-select selectEmployment" aria-label="Default select example"
                            value={employment_id} onChange={chooseEmployment}>
                        {optionsEmployment.map(option => (
                            <option key={option.value} value={option.value}>
                                {option.text}
                            </option>
                        ))}
                    </select>
                    <select className="form-select selectPosition" aria-label="Default select example"
                            value={position_id} onChange={choosePosition}>
                        {optionsPosition.map(option2 => (
                            <option key={option2.value} value={option2.value}>
                                {option2.text}
                            </option>
                        ))}
                    </select>
                </form>
                <button className="btn btn-primary btnAddEmployee" onClick={postData}> Register</button>
            </div>
        </div>
    );
}

export default AddEmployee;