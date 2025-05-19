from flask import Flask, send_from_directory, jsonify
import sqlite3
import os

app = Flask(__name__, static_folder='static')
DB_PATH = os.path.join(os.path.dirname(__file__), 'chores.db')

# Serve child and parent pages
@app.route('/')
def home():
    return send_from_directory('static', 'tyler.html')

@app.route('/tyler')
def tyler():
    return send_from_directory('static', 'tyler.html')

@app.route('/charlotte')
def charlotte():
    return send_from_directory('static', 'charlotte.html')

@app.route('/parent')
def parent():
    return send_from_directory('static', 'parent.html')

# ✅ API route: Get chores for a child
@app.route('/api/chores/<child>')
def get_chores(child):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute('''
        SELECT id, title, reward, assigned_to, expires_by, days_required, notes
        FROM chores
        WHERE assigned_to = ? AND active = 1
        ORDER BY priority ASC, id ASC
    ''', (child.capitalize(),))

    chores = [dict(row) for row in cursor.fetchall()]
    conn.close()

    return jsonify(chores)

from flask import request

@app.route('/api/chores', methods=['POST'])
def add_chore():
    data = request.get_json()

    title = data.get("title")
    reward = data.get("reward")
    assigned_to = data.get("assigned_to")
    days_required = data.get("days_required", None)
    expires_by = data.get("expires_by", None)
    notes = data.get("notes", None)

    if not (title and reward and assigned_to):
        return {"error": "Missing required fields"}, 400

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO chores (
            title, reward, assigned_to, active,
            expires_by, days_required, notes
        ) VALUES (?, ?, ?, 1, ?, ?, ?)
    ''', (title, reward, assigned_to, expires_by, days_required, notes))

    conn.commit()
    conn.close()
    return {"success": True}, 201

@app.route('/api/chores/<int:chore_id>/deactivate', methods=['POST'])
def deactivate_chore(chore_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('UPDATE chores SET active = 0 WHERE id = ?', (chore_id,))
    conn.commit()
    conn.close()
    return {"success": True}

@app.route('/api/chores/<int:chore_id>/assign', methods=['POST'])
def reassign_chore(chore_id):
    data = request.get_json()
    new_assigned_to = data.get('assigned_to')
    if not new_assigned_to:
        return {"error": "Missing assigned_to"}, 400

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('UPDATE chores SET assigned_to = ? WHERE id = ?', (new_assigned_to, chore_id))
    conn.commit()
    conn.close()
    return {"success": True}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
