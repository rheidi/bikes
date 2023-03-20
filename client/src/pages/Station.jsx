import React, { useState, useEffect } from "react"
import { useParams } from "react-router-dom"

function Station() {
    const id = useParams().id
    const [data, setData] = useState([{}])

    useEffect(() => {
    fetch("/station_info/"+id).then(
        res => res.json()
    ).then(
        data => {
            setData(data)
            console.log(data)
        }
    )
    }, [])
    return (
        <div>
            {(typeof data.station_info === 'undefined') ? (
                <p>Loading...</p>
                ) : (
                    <>
                        <b>Station name:</b>
                        <p>{data.station_info.nimi}</p>
                        <b>Station address:</b>
                        <p>{data.station_info.osoite}</p>
                    </>
                )
            }
        </div>
    )
}

export default Station