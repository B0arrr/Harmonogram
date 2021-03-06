import React, {useEffect, useState} from "react";
import Axios from "axios";
import '../Components/Style/Schedule.css';

function Schedule() {

    const [data2, setData2] = useState([]);


    useEffect(() => {
        Axios.get(`http://localhost:8000/api/get_generated_schedule/start/${localStorage.getItem('inputValue')}/end/${localStorage.getItem('inputValue2')}?department=${localStorage.getItem('inputValue3')}`)
            .then(res => {
                console.log("Getting from :::", res.data);
                setData2(res.data);
            }).catch(err => console.log(err));
    }, []);



    return (
        <div>
            <h1>Schedule:</h1>
            <div className="containerSchedule">
                {data2.schedules?.map((item2, i2) => (
                    <table className="table table-bordered  tableSchedule">
                        <thead>
                        <tr className="bg-light-gray" key={i2}>
                            <div className="dayInSchedule"><strong>Date: {item2.day}</strong></div>
                            <th>Name:
                                {item2.employees?.map((item3, i3) => (
                                   <tr key={i3}>
                                       <th>
                                           {item3.name}
                                       </th>
                                   </tr>
                                    ))}
                            </th>
                            <th>Surname:
                                {item2.employees?.map((item3, i3) => (
                                    <tr>
                                        <th>
                                            {item3.surname}
                                        </th>
                                    </tr>
                                    ))}
                            </th>
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