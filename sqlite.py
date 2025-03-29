import sqlite3

# Connect to the database (it will create the database file if it doesn't exist)
connection = sqlite3.connect("student.db")
cursor = connection.cursor()

# Create the student table if it doesn't already exist
table_info = """CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY,
    name VARCHAR(50),
    age INTEGER,
    marks INTEGER,
    class VARCHAR(25),
    section VARCHAR(25)
)"""

# Execute the table creation
cursor.execute(table_info)

# Insert data into the student table
cursor.execute("INSERT INTO student(name, age, marks, class, section) VALUES('Rahul', 15, 85, '10th', 'A')")
cursor.execute("INSERT INTO student(name, age, marks, class, section) VALUES('Rohit', 16, 75, '10th', 'B')")
cursor.execute("INSERT INTO student(name, age, marks, class, section) VALUES('Raj', 15, 65, '10th', 'C')")
cursor.execute("INSERT INTO student(name, age, marks, class, section) VALUES('Ravi', 16, 55, '10th', 'A')")
cursor.execute("INSERT INTO student(name, age, marks, class, section) VALUES('Raman', 15, 45, '10th', 'B')")
cursor.execute("INSERT INTO student(name, age, marks, class, section) VALUES('Rajesh', 16, 35, '10th', 'C')")
cursor.execute("INSERT INTO student(name, age, marks, class, section) VALUES('Rajiv', 15, 25, '10th', 'A')")

# Commit the changes
connection.commit()

# Fetch and print all data from the student table
data = cursor.execute("SELECT * FROM student")
for row in data:
    print(row)

# Close the connection
connection.close()