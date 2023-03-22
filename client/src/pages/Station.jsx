import React, { useState, useEffect } from "react"
import { useParams } from "react-router-dom"

function Station() {
    const id = useParams().id
    const [data, setData] = useState([{}])

    useEffect(() => {
    fetch("/station_info/"+id)
    .then(res => res.json())
    .then(data => setData(data))
    }, [])
    return (
        <div>
            {(typeof data === 'undefined') ? (
                <p>Loading...</p>
                ) : (
                    <>
                        <b>Station name:</b>
                        <p>{data.nimi}</p>
                        <b>Station address:</b>
                        <p>{data.osoite}</p>
                    </>
                )
            }
        </div>
    )
}

export default Station