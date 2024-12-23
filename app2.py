from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# API endpoint to get all entries from the database
@app.route('/api/entries', methods=['GET'])
def get_entries():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM entries')
    entries = cursor.fetchall()
    conn.close()
    
    # Return entries as JSON to be used by the frontend
    return jsonify(entries)

# API endpoint to handle form submission
@app.route('/api/submit', methods=['POST'])
def submit_entry():
    name = request.json.get('name')
    email = request.json.get('email')
    message = request.json.get('message')

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO entries (name, email, message) VALUES (?, ?, ?)
    ''', (name, email, message))
    conn.commit()
    conn.close()

    return jsonify({"status": "success"})

# API endpoint to delete an entry
@app.route('/api/delete/<int:id>', methods=['DELETE'])
def delete_entry(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM entries WHERE id = ?', (id,))
    conn.commit()
    conn.close()

    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
