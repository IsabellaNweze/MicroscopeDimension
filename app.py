from flask import Flask, render_template, request, redirect, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Setup database
def setup_database():
    conn = sqlite3.connect("specimens.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS specimen_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            specimen_name TEXT NOT NULL,
            microscope_size REAL NOT NULL,
            magnification REAL NOT NULL,
            actual_size REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Home Route
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            username = request.form["username"]
            specimen = request.form["specimen"]
            microscope_size = float(request.form["microscope_size"])
            magnification = float(request.form["magnification"])

            if magnification <= 0:
                flash("Magnification must be greater than 0.")
                return redirect("/")

            actual_size = microscope_size / magnification

            conn = sqlite3.connect("specimens.db")
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO specimen_data (username, specimen_name, microscope_size, magnification, actual_size)
                VALUES (?, ?, ?, ?, ?)
            """, (username, specimen, microscope_size, magnification, actual_size))
            conn.commit()
            conn.close()

            flash(f"Saved successfully! Real-life size: {actual_size:.4f} μm")
            return redirect("/")
        except:
            flash("Error: Please enter valid data.")
            return redirect("/")

    return render_template("index.html")

if __name__ == "__main__":
    setup_database()
    app.run(debug=True)
