import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        roll INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        course TEXT NOT NULL
        )
""")

cursor.execute("INSERT INTO students VALUES(12345,'Aditya','c')")
cursor.execute("INSERT INTO students VALUES(12346,'Akash','it')")
cursor.execute("INSERT INTO students VALUES(12347,'Adarsh','c')")

conn.commit()
cursor.execute("SELECT * FROM students")

print("Student details:")
for row in cursor.fetchall():
    print(row)

conn.close()

# conn.cursor() -> conn.commit() -> conn.close()
# for row in cursor.fetchall(): 
#     print(row)
