import sqlite3

# Database Connection
conn = sqlite3.connect('orders.db')

# Cursor Object
cur = conn.cursor()

# Create Table if none exists
cur.execute("""CREATE TABLE IF NOT EXISTS recorder(
            recorder_id INT PRIMARY KEY,
            month DATE,
            day INT,
            year INT,
            hours REAL,
            aldi TEXT,
            afton TEXT);
""")

conn.commit()

# Class for adding a new entry into the database
#   Default Constructor
#   User Constructor
#   List, retrieve, edit, and delete functions
#   Function to input 
class Entry():
    def __init__(self, entry) -> None:
        self.entry = entry


# Function to show record entry page

# Function to show database, maybe only last 10-20 entries

# Menu function
def menu():
    print("What would you like to do?")
    print()
    print("(1) Add new entry")
    print("(2) View all entries")
    print("(3) Edit an entry")
    print("(4) Delete an entry")

    entry = int(input("What say you? "))
    return entry

# Start page
def startPage():
    print("Welcome to your Programming Recorder. Here you can input how much you coded for the day and we will keep track for you.")
    print()

# Main function
def main():
    startPage()
    entry = menu()
    print(entry)

if __name__ == '__main__':
    main()