import pandas as pd
import db

def main():
    df = pd.read_csv('stations.csv')
    conn = db.get_db_connection()
    df.to_sql("stations", conn)

if __name__ == "__main__":
    main()
