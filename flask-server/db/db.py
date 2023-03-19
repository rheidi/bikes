import sqlite3

def get_db_connection():
    conn = sqlite3.connect('db/stations.db')
    print("yhteys onnistui!")
    return conn

def get_stations():
    conn = get_db_connection()
    cur = conn.cursor()
    stations = cur.execute('SELECT Nimi FROM stations').fetchall()
    conn.close()
    return stations
