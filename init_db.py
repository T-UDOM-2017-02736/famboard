import sqlite3

conn = sqlite3.connect('chores.db')
cursor = conn.cursor()

# --- Chores Table ---
cursor.execute('''
CREATE TABLE IF NOT EXISTS chores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    reward REAL NOT NULL,
    assigned_to TEXT NOT NULL,
    active INTEGER NOT NULL DEFAULT 1,
    expires_by TEXT,
    days_required TEXT,
    notes TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    completed_by TEXT,
    repeat_interval TEXT,
    group_id INTEGER,
    priority INTEGER
)
''')
print("✅ chores table created")

# Sample chores
starter_chores = [
    ("Make bed", 1.00, "Child1", 1, None, "Daily", None, None, None, None, None),
    ("Feed pet", 1.00, "Child1", 1, None, "Daily", None, None, None, None, None),
    ("Take out trash", 1.50, "Child1", 1, None, "Wed", "Take out before 6pm", None, None, None, 2),
    ("Homework", 2.00, "Child1", 1, None, "Mon,Tue,Wed,Thu", None, None, None, None, 1),
    ("Clean up toys", 1.00, "Child2", 1, None, "Daily", None, None, None, None, None),
    ("Feed the cat", 1.00, "Child2", 1, None, "Daily", None, None, None, None, None),
    ("Set the table", 1.50, "Child2", 1, None, "Fri", None, None, None, None, 2),
    ("Brush hair", 2.00, "Child2", 1, None, "Daily", None, None, None, None, 1)
]

cursor.executemany('''
INSERT INTO chores (
    title, reward, assigned_to, active,
    expires_by, days_required, notes, completed_by,
    repeat_interval, group_id, priority
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', starter_chores)
print("✅ sample chores inserted")

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
    child TEXT,
    description TEXT,
    target_amount REAL,
    saved_amount REAL
)
''')
print("✅ goals table created")

conn.commit()
conn.close()
print("✅ All tables created and initialized.")
