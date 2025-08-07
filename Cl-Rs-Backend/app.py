from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)
DB_NAME = 'views.db'

# Initialize DB
def init_db():
    conn = sqlite3.connect('views.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS views (count INTEGER)')
    cur.execute('SELECT COUNT(*) FROM views')
    if cur.fetchone()[0] == 0:
        cur.execute('INSERT INTO views (count) VALUES (0)')
    conn.commit()
    conn.close()

init_db()  # <--- call it at the module level

@app.route('/views', methods=['GET'])
def count_views():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('SELECT count FROM views')
    count = cur.fetchone()[0]
    count += 1
    cur.execute('UPDATE views SET count = ?', (count,))
    conn.commit()
    conn.close()
    return jsonify({'views': count})





