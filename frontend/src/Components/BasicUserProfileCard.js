import './Style/UserProfileCard.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import React, {useEffect, useState} from "react";
import Axios from "axios";
import Login from "../test/Login";


function BasicUserProfileCard() {

    const  [data, setData] = useState([])




    useEffect(() =>{
        const token = localStorage.getItem('temitope')
        Axios.get(`http://localhost:8000/api/get_employee_by_email/${localStorage.getItem('inputEmailValue')}`,{ headers: {"Authorization" : `Bearer ${token}`} })
            .then(res => {
                console.log(res.data)
                setData(res.data)
            })
            .catch((error) =>{
                console.log(error);
            })
    },[])
console.log(data.employment_id)
    const aa = data.position_id
    function test(){
        if (aa === 1){
            return true
        } else {
            return false
        }
    }


    return (
        <div>
            <div className="myProfile">
                <div className="myProfileContainer">
                    <div className="myProfileBorder">
                        <div className="splitDataIntoColumns">
                            <div className="infoAboutEmployee">
                                <p className="employeeInfoHeader"> {data.name} {data.surname}: </p>
                                <p>ID: {data.id}</p>
                                <p>Position: {data.position_id == 1 && <>Kierownik</> } {data.position_id == 2 && <>Pracownik</> }</p>
                            </div>
                            <div className="infoAboutAccount">
                                <p className="accountInfoHeader"> Info about account: </p>
                                <p>Login:  {data.login}</p>
                                <p>E-mail: {data.email}</p>
                                <p>Department: {data.department}</p>
                                <p>Etat: {data.employment_id== 1  && <> Cały etat</>} {data.employment_id == 2  && <> 3/4 etatu</>} {data.employment_id == 3  && <> Pół etatu</>} {data.employment_id == 4  && <> 1/4 etat</>}<br/></p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}


export default BasicUserProfileCard;