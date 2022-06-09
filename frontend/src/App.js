import React, {useContext} from 'react';
import Login from "./Components/TestLogin/Login";
import HeaderLogin from "./Components/Header/HeaderLogin";
import {UserContext} from "./Components/TestLogin/UserContext";



function App() {
const [token] = useContext(UserContext)
    return (
        <div>
            <HeaderLogin/>
            <div>
                <div>
                        <div>
                            <p><Login/></p>
                        </div>
                </div>
            </div>
            {/*<Login/>*/}
        </div>

    );
}

export default App;


