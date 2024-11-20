import sqlite3
from flask import Flask, jsonify, g

app = Flask(__name__)

# Polku SQLite-tietokantaan
DATABASE = 'airports.db'

def get_db():
    """Yhdistä tietokantaan ja palauta yhteys."""
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    """Sulje tietokantayhteys sovelluksen sulkemisen yhteydessä."""
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/kenttä/<string:icao>', methods=['GET'])
def get_airport(icao):
    """Hae lentokentän tiedot ICAO-koodin perusteella."""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT icao, name, municipality FROM airport WHERE icao = ?", (icao.upper(),))
    row = cursor.fetchone()
    if row:
        result = {"ICAO": row[0], "Name": row[1], "Municipality": row[2]}
    else:
        result = {"error": "Airport not found"}
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)
