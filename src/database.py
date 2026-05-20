import sqlite3

DB_PATH = "data/trips.db"


def create_trips_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS trips (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            destination TEXT,
            budget REAL,
            days INTEGER,
            transport TEXT,
            stay_type TEXT,
            cuisine TEXT,
            total_cost REAL,
            remaining_budget REAL
        )
    """)

    conn.commit()
    conn.close()


def save_trip(destination, budget, days, transport, stay_type, cuisine, total_cost, remaining_budget):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO trips (
            destination, budget, days, transport, stay_type, cuisine, total_cost, remaining_budget
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        destination, budget, days, transport, stay_type, cuisine, total_cost, remaining_budget
    ))

    conn.commit()
    conn.close()

    
def get_all_trips():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT destination, budget, days, transport, stay_type, cuisine, total_cost, remaining_budget
        FROM trips
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    return rows