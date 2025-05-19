import sqlite3

conn = sqlite3.connect('chores.db')
cursor = conn.cursor()

# --- Users Table ---
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
''')
print("✅ users table created")

# --- Chores Table ---
cursor.execute('''
CREATE TABLE IF NOT EXISTS chores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    reward REAL NOT NULL,
    assigned_to INTEGER NOT NULL,
    active INTEGER NOT NULL DEFAULT 1,
    expires_by TEXT,
    days_required TEXT,
    notes TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    completed_by TEXT,
    repeat_interval TEXT,
    group_id INTEGER,
    priority INTEGER,
    FOREIGN KEY (assigned_to) REFERENCES users(id)
)
''')
print("✅ chores table created")

# --- Meals Table ---
cursor.execute('''
CREATE TABLE IF NOT EXISTS meals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    day TEXT,
    meal TEXT,
    type TEXT
)
''')
print("✅ meals table created")

# --- Events Table ---
cursor.execute('''
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    title TEXT,
    time TEXT,
    details TEXT
)
''')
print("✅ events table created")

# --- Goals Table ---
cursor.execute('''
CREATE TABLE IF NOT EXISTS goals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    description TEXT,
    target_amount REAL,
    saved_amount REAL,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
''')
print("✅ goals table created")

conn.commit()
conn.close()
print("\u2705 All tables created and initialized.")
