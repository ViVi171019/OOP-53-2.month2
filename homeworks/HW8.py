import sqlite3

connect = sqlite3.connect('Staffs.db')
cursor = connect.cursor()
cursor.execute('''
   CREATE TABLE IF NOT EXISTS staffs(
        staffid INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER NOT NULL,
        birthday TEXT
   )
''')
cursor.execute('''
   CREATE TABLE IF NOT EXISTS shifts(
        shiftid INTEGER PRIMARY KEY,
        start_time TEXT,
        end_time TEXT,
        staff_id INTEGER,
        FOREIGN KEY (staff_id) REFERENCES staffs(staffid)
   )
''')