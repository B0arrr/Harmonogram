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
                    <div className='aadawdawd'>
                    <div className='testasad'>
                        <h1>Jan Kowalski</h1>
                        <div className='infoAboutWorker'>
                           <p>Position: Kierownik</p>
                           <p>ID: 111</p>
                        </div>
                    </div>
                    <div className='infoAboutAccount'>
                        <p className='accountInfoHeader'> Info about account: </p>
                           <p>Name: Maciek</p>
                           <p>Surname: Kowalczyk</p>
                           <p>E-mail: kowalczyk_maciej@ppp.pl</p>
                           <p>Login: Maciek31</p>
                           <p></p>
                    </div>
                   </div>
                    </div>
                </div>
            </div>
            </div>
    )
}

export default MyProfile