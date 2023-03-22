import pandas as pd
import db

def main():
    df_stations = pd.read_csv('db/stations.csv')
    conn_stations = db.get_db_connection('db/stations.db')
    df_stations.to_sql("stations", conn_stations)
    conn_stations.close()

    df_journeys = pd.read_csv("db/2021-05.csv")
    conn_journeys = db.get_db_connection("db/journeys.db")
    df_journeys[(df_journeys["Covered distance (m)"] >= 10) & (df_journeys["Duration (sec.)"] >= 10)].to_sql("journeys", conn_journeys)
    conn_journeys.close()

if __name__ == "__main__":
    main()
