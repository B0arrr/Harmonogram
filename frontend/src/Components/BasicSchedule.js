import React, {useEffect, useState} from "react";
import Axios from "axios";
import '../Components/Style/BasicSchedule.css';

function Schedule() {

    const [data2, setData2] = useState([]);


    useEffect(() => {
        Axios.get(`http://localhost:8000/api/get_generated_schedule/start/${localStorage.getItem('inputValue')}/end/${localStorage.getItem('inputValue2')}/employee_id/${localStorage.getItem('idEmployee')}`)
            .then(res => {
                console.log("Getting from :::", res.data);
                setData2(res.data);
            }).catch(err => console.log(err));
    }, []);


    return (
        <div>
            <div className="containerSchedule">
                {data2.schedules?.map((item2, i2) => (
                    <table className="table table-bordered  tableSchedule">
                        <thead>
                        <tr className="bg-light-gray" key={i2}>
                            <th className="dayInSchedule">Date: {item2.day}</th>
                            <th className='nameInSchedule'>Name: {item2.employee?.name}</th>
                            <th>Surname: {item2.employee?.surname}</th>
                            <th className="dayInSchedule">Shift: {item2.shift}</th>

                        </tr>
                        </thead>
                    </table>
                ))}

            </div>
        </div>


        // <div className="containerForSchedule">
        //     <h4 className="scheduleGenerate">
        //         {data2.schedules?.map((item2, i2) => (
        //             <ul className="scheduleUl" key={i2}>
        //                 <li className="scheduleLi">
        //                     <div className="scheduleDisplayDay">
        //                         <p><strong>Day:</strong></p>
        //                         <p><strong>Employee in work:</strong></p>
        //                     </div>
        //                     <div className="test">
        //
        //                         {item2.day}
        //                         {item2.employees?.map((item3, i3) => (
        //
        //                             <ul className="scheduleUl" key={i3}>
        //
        //                                 <li className="scheduleLi">
        //                                     Name: {item3.name} <br/>
        //                                     Surname: {item3.surname}
        //                                 </li>
        //                             </ul>
        //                         ))}
        //                     </div>
        //                 </li>
        //             </ul>
        //         ))}
        //     </h4>
        // </div>



    );
}


export default Schedule;