import './App.css';
import {useEffect, useState} from "react";
import json from "qs";

function App() {
    const [name, setName] = useState()

    useEffect(() => {
        const fetchData = async () => {
            const data = await (await fetch("http://localhost:8000/api/")).json()
            setName(data.name)
        }

        fetchData().then()
    }, [])

    return (
        <div className="App">
            <h1>Cześć, {name}</h1>
        </div>
    );
}

export default App;
