
import os
import sqlite3
from flask import Flask, jsonify, request, g


app = Flask(__name__)

app.config["DATABASE"] = os.environ.get("DATABASE_PATH", "gym.db")


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(error=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()
    db.execute("""
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT
        )
    """)
    db.commit()


@app.route("/")
def home():
    return "<h1>Welcome to ACEest Fitness & Gym!</h1>"


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/members", methods=["POST"])
def register_member():
    data = request.get_json(silent=True) or {}

    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    phone = data.get("phone", "").strip()

    if not name or not email:
        return jsonify({
            "error": "Name and email are required"
        }), 400

    db = get_db()

    try:
        cursor = db.execute(
            "INSERT INTO members (name, email, phone) VALUES (?, ?, ?)",
            (name, email, phone)
        )
        db.commit()

        return jsonify({
            "message": "Member registered successfully",
            "member_id": cursor.lastrowid,
            "name": name,
            "email": email
        }), 201

    except sqlite3.IntegrityError:
        return jsonify({
            "error": "A member with this email already exists"
        }), 409



@app.route("/members", methods=["GET"])
def get_members():
    db = get_db()

    search = request.args.get("search", "").strip()

    if search:
        search_term = f"%{search}%"

        members = db.execute(
            """
            SELECT * FROM members
            WHERE name LIKE ? OR email LIKE ?
            ORDER BY id
            """,
            (search_term, search_term)
        ).fetchall()
    else:
        members = db.execute(
            "SELECT * FROM members ORDER BY id"
        ).fetchall()

    return jsonify([dict(member) for member in members])



with app.app_context():
    init_db()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
