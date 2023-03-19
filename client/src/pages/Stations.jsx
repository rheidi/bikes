import React, { useState, useEffect } from "react"

function Stations() {
    const [data, setData] = useState([{}])

    useEffect(() => {
    fetch("/stations").then(
        res => res.json()
    ).then(
        data => {
        setData(data)
        
        console.log("data",data)
        }
    )
    }, [])
    return (
        <div>
            {(typeof data.stations === 'undefined') ? (
            <p>Loading...</p>
            ) : [
                data.stations.map((station, i) => (
                <p key={i}>{station}</p>
                ))
            ]}
        </div>
    )
}

export default Stations