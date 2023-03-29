import React, { useMemo, useState, useEffect } from "react"
import { useParams } from "react-router-dom"
import Table from "../components/Table"

function Station() {
    const id = useParams().id
    const columns = useMemo(
        () => [
            {
                Header: "Station name",
                accessor: "nimi",
            },
            {
                Header: "Station address",
                accessor: "osoite"
            },
            {
                Header: "Journeys starting from here",
                accessor: "departures"
            },
            {
                Header: "Journeys ending here",
                accessor: "returns",
            },
        ], []
    )
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
                <Table columns={columns} data={[data]} />
            )}
        </div>
    )
}

export default Station
