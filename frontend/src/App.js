import { Routes, Route } from "react-router-dom";
import { RequireToken } from "./test/Auth";
import Login from "./test/Login";
import Profile from "./test/Profile";

function App(){



    return(
        <div className ="App">
            <Routes>
                <Route path="/" element = {<Login/>}/>
                <Route path="/profile" element = {
                   <RequireToken>
                       <Profile/>
                   </RequireToken>

                }/>
            </Routes>
        </div>
    )
}






// import React from 'react';
// import Login from "./Components/Login";
// import HeaderLogin from "./Components/Header/HeaderLogin";
//
//
//
//
// function App() {
//     return (
//         <div>
//             <HeaderLogin/>
//             <Login/>
//         </div>
//
//     );
// }

export default App;


