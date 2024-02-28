import sqlite3

# Function to create the database table
def create_table():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contacts
                 (ID INTEGER PRIMARY KEY, Name TEXT, Cell TEXT, Email TEXT)''')
    conn.commit()
    conn.close()

# Function to insert data into the table
def insert_data(name, cell, email):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("INSERT INTO contacts (Name, Cell, Email) VALUES (?, ?, ?)", (name, cell, email))
    conn.commit()
    conn.close()

# Function to fetch all data from the table
def fetch_data():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM contacts")
    data = c.fetchall()
    conn.close()
    return data

# Create table if not exists
create_table()

# Insert 5 rows of data
insert_data("Jhon", "1234567891", "john@gmail.com")
insert_data("Jack", "1234567892", "alice@gmail.com")
insert_data("Bob ", "5551234567", "bob@gmail.com")
insert_data("Brijesh D", "4445556666", "brijesh@gmail.com")
insert_data("Michael Brown", "7778889999", "michael@gmail.com")

# Fetch and display all data
print("ID\tName\t\tCell#\t\t\tEmail")
print("-" * 50)
for row in fetch_data():
    print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")
