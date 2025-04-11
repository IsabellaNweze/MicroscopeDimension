import sqlite3

# Setup: Create/connect to database and table
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

# Main logic: Get input, calculate actual size, and store it
def store_specimen_data():
    try:
        username = input("Enter your username: ")
        specimen_name = input("Enter specimen name: ")
        microscope_size = float(input("Enter microscope size (μm): "))
        magnification = float(input("Enter magnification: "))

        if magnification <= 0:
            print("Magnification must be greater than 0.")
            return

        actual_size = microscope_size / magnification
        print(f"Calculated real-life size: {actual_size:.4f} μm")

        conn = sqlite3.connect("specimens.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO specimen_data (username, specimen_name, microscope_size, magnification, actual_size)
            VALUES (?, ?, ?, ?, ?)
        """, (username, specimen_name, microscope_size, magnification, actual_size))
        conn.commit()
        conn.close()
        print("Data successfully stored in database.")
    except ValueError:
        print("Please enter valid numbers.")
    except Exception as e:
        print("An error occurred:", e)

# Run the full program
setup_database()
store_specimen_data()
