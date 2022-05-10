import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import Register from "./Pages/Register";
import Logged from "./Pages/Logged";
import MyProfile from "./Pages/MyProfile";



const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
         <Router>
         <Routes>
             <Route path='/' element ={<App/>}/>
             <Route path='/src/Pages/Register' element={<Register/>}/>
             <Route path='/src/Pages/Logged' element={<Logged/>}/>
             <Route path='/src/Pages/MyProfile' element={<MyProfile/>}/>


         </Routes>
         </Router>
        </React.StrictMode>
);


// const root = ReactDOM.createRoot(document.getElementById('root'));
// root.render(
//   <React.StrictMode>
//     <App />
//
//   </React.StrictMode>
// );

reportWebVitals();
