import React from "react";
import { HeaderMyProfile} from "../Components/Header";
import '../Components/MyProfile.css'
import 'bootstrap/dist/css/bootstrap.min.css';


function MyProfile() {

    return(
            <div>
                <HeaderMyProfile/>
                <div className='myProfile'>
                <div className='myProfileContainer'>
                    <div className='myProfileBorder'>
                    <div className='splitDataIntoColumns'>
                        <div className='infoAboutEmployee'>
                            <p className='employeeInfoHeader'> Jan Kowalski: </p>
                            <p>ID: 1</p>
                            <p>Position: Kierownik</p>
                        </div>
                    <div className='infoAboutAccount'>
                        <p className='accountInfoHeader'> Info about account: </p>
                           <p>Name: Maciek</p>
                           <p>Surname: Kowalczyk</p>
                           <p>E-mail: kowalczyk_maciej@p.pl</p>
                           <p>Login: Maciek31</p>
                    </div>
                   </div>
                    </div>
                </div>
            </div>
            </div>
    )
}

export default MyProfile