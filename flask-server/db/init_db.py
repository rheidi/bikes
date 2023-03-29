import pandas as pd
import db

def main():
    df_stations = pd.read_csv('db/stations.csv')
    conn = db.get_db_connection('db/bikes.db')
    df_stations.to_sql("stations", conn)
    df_journeys = pd.read_csv("db/2021-05.csv")
    df_journeys[(df_journeys["Covered distance (m)"] >= 10) & (df_journeys["Duration (sec.)"] >= 10)].to_sql("journeys", conn)
    conn.close()

if __name__ == "__main__":
    main()
