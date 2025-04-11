import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database setup
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

# Store data function
def store_data():
    try:
        username = entry_username.get()
        specimen_name = entry_specimen.get()
        microscope_size = float(entry_microscope.get())
        magnification = float(entry_magnification.get())

        if magnification <= 0:
            raise ValueError("Magnification must be greater than 0.")

        actual_size = microscope_size / magnification

        conn = sqlite3.connect("specimens.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO specimen_data (username, specimen_name, microscope_size, magnification, actual_size)
            VALUES (?, ?, ?, ?, ?)
        """, (username, specimen_name, microscope_size, magnification, actual_size))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", f"Data saved!\nReal-life size: {actual_size:.4f} μm")
        clear_fields()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def clear_fields():
    entry_username.delete(0, tk.END)
    entry_specimen.delete(0, tk.END)
    entry_microscope.delete(0, tk.END)
    entry_magnification.delete(0, tk.END)

# GUI setup
setup_database()
window = tk.Tk()
window.title("Microscope Specimen Size Calculator")

tk.Label(window, text="Username:").grid(row=0, column=0, sticky="e")
tk.Label(window, text="Specimen Name:").grid(row=1, column=0, sticky="e")
tk.Label(window, text="Microscope Size (μm):").grid(row=2, column=0, sticky="e")
tk.Label(window, text="Magnification:").grid(row=3, column=0, sticky="e")

entry_username = tk.Entry(window)
entry_specimen = tk.Entry(window)
entry_microscope = tk.Entry(window)
entry_magnification = tk.Entry(window)

entry_username.grid(row=0, column=1)
entry_specimen.grid(row=1, column=1)
entry_microscope.grid(row=2, column=1)
entry_magnification.grid(row=3, column=1)

tk.Button(window, text="Calculate & Save", command=store_data).grid(row=4, column=0, columnspan=2, pady=10)

window.mainloop()
