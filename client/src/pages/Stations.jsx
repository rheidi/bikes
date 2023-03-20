import React, { useState, useEffect } from "react"
import { Link } from "react-router-dom"

function Stations() {
    const [data, setData] = useState([{}])

    useEffect(() => {
    fetch("/stations").then(
        res => res.json()
    ).then(
        data => {
            setData(data)
        }
    )
    }, [])
    return (
        <div>
            <ul>
                {(typeof data.stations === 'undefined') ? (
                <p>Loading...</p>
                ) : (
                    data.stations.map(station =>
                        <li key={station.id}>
                            <Link to={"/stations/"+station.id}>{station.nimi}</Link>
                        </li>
                    )
                )}
            </ul>
        </div>
    )
}

export default Stations