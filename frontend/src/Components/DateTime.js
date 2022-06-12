import React from "react";

export default function DateTime() {
    const current = new Date();
    const date = `${current.getDate()}/${current.getMonth() + 1}/${current.getFullYear()}`;

    return (
        <div className="DateTime">
            <h1>Current date is {date}</h1>
        </div>
    );
}