import sqlite3

def get_db_connection():
    conn = sqlite3.connect('db/stations.db')
    print("yhteys onnistui!")
    return conn

def get_stations():
    conn = get_db_connection()
    cur = conn.cursor()
    result = cur.execute('SELECT ID, Nimi FROM stations').fetchall()
    stations = [dict(zip([key[0].lower() for key in cur.description], row)) for row in result]
    conn.close()
    return stations

def get_station_info(id):
    conn = get_db_connection()
    cur = conn.cursor()
    result = cur.execute('SELECT Nimi, Osoite FROM stations WHERE ID=?', [id]).fetchone()
    station_info = dict(zip([key[0].lower() for key in cur.description], result))
    conn.close()
    return station_info