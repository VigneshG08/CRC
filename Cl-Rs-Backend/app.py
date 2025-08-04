from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)
DB_NAME = 'views.db'

# Initialize DB
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS views (count INTEGER)')
    cur.execute('SELECT * FROM views')
    if not cur.fetchone():
        cur.execute('INSERT INTO views (count) VALUES (0)')
    conn.commit()
    conn.close()

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

    init_db()  # <--- call it at the module level

