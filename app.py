from flask import Flask, request, jsonify, render_template
import mysql.connector
import os

app = Flask(__name__)

db_config = {
    "host": os.environ.get("DB_HOST", "localhost"),
    "user": os.environ.get("DB_USER", "root"),
    "password": os.environ.get("DB_PASS", ""),
    "database": os.environ.get("DB_NAME", "notesdb"),
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_note():
    data = request.get_json()
    content = data.get("content")

    if not content:
        return jsonify({"error": "No content provided"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes (content) VALUES (%s)", (content,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Note added successfully"}), 201

@app.route("/notes", methods=["GET"])
def get_notes():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, content FROM notes")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    notes = [{"id": row[0], "content": row[1]} for row in rows]
    return jsonify(notes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

