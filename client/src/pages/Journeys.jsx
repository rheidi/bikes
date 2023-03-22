import React, { useMemo, useState, useEffect } from "react"
import Table from "../components/Table"

function Journeys() {
    const columns = useMemo(
        () => [
            {
                Header: "Departure station",
                accessor: "departure",
            },
            {
                Header: "Return station",
                accessor: "return"
            },
            {
                Header: "Distance",
                accessor: "distance"
            },
            {
                Header: "Duration",
                accessor: "duration",
            },
        ], []
    )
    const [data, setData] = useState([{}])

    useEffect(() => {
        fetch("/journeys")
        .then(res => res.json())
        .then(data => setData(data))
    }, [])
    return (
        <div>
            {(typeof data.journeys === 'undefined') ? (
            <p>Loading...</p>
            ) : (
                <Table columns={columns} data={data.journeys} />
            )}
        </div>
    )
}

export default Journeys
