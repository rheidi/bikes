from flask import Flask
from db import db

app = Flask(__name__)

@app.route("/stations")
def stations():
    stationslist = db.get_stations()
    return {"stations": stationslist}

if __name__ == "__main__":
    app.run(debug=True)