import sqlite3

def get_db_connection(name):
    conn = sqlite3.connect(name)
    print("yhteys onnistui!")
    return conn

def get_stations():
    conn = get_db_connection('db/bikes.db')
    cur = conn.cursor()
    result = cur.execute('SELECT ID, Nimi FROM stations').fetchall()
    stations = [dict(zip([key[0].lower() for key in cur.description], row)) for row in result]
    conn.close()
    return stations

def get_station_info(id):
    conn = get_db_connection('db/bikes.db')
    cur = conn.cursor()
    result = cur.execute("""SELECT
    s.ID,
    s.Nimi,
    s.Osoite,
    (SELECT COUNT(*) FROM journeys WHERE "Departure station id" = s.ID) as departures,
    (SELECT COUNT(*) FROM journeys WHERE "Return station id" = s.ID) as returns
    FROM stations s WHERE s.ID=?""", [id]).fetchone()
    station_info = dict(zip([key[0].lower() for key in cur.description], result))
    conn.close()
    return station_info

def get_journeys():
    conn = get_db_connection("db/bikes.db")
    cur = conn.cursor()
    result = cur.execute('SELECT "Departure station name", "Return station name", "Covered distance (m)", "Duration (sec.)" FROM journeys').fetchmany(1000)
    journeys = [dict(zip(["departure", "return", "distance", "duration"], row)) for row in result]
    conn.close()
    return journeys
