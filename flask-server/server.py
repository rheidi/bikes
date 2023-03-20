from flask import Flask
from db import db

app = Flask(__name__)

@app.route("/stations")
def stations():
    stationslist = db.get_stations()
    return {"stations": stationslist}

@app.route("/station_info/<id>")
def station_info(id):
    info = db.get_station_info(id)
    return {"station_info": info}

if __name__ == "__main__":
    app.run(debug=True)