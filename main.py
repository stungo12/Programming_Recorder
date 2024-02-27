import sqlite3

# Database Connection
conn = sqlite3.connect('orders.db')

# Cursor Object
cur = conn.cursor()

# Create Table if none exists
cur.execute("""CREATE TABLE IF NOT EXISTS recorder(
            recorder_id INT PRIMARY_KEY,
            month INT,
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
    def __init__(self, id, month, day, year, time, notes):
        self.id = id
        self.month = month
        self.day = day
        self.year = year
        self.time = time
        self.notes = notes

    def add(self):
        print("ADD")

        # Have the user input their time log information into the system
        self.id = int(input("Recorder ID: "))
        self.month = int(input("Month: "))
        self.day = int(input("Day: "))
        self.year = int(input("Year: "))
        self.time = int(input("Amount of time spent programming: "))

        # Take the user input and add it to the database
        cur.execute(f"""INSERT INTO recorder(recorder_id, month, day, year, time, notes)
                    VALUES ({self.id}, {self.month}, {self.day}, {self.year}, {self.time}, {self.notes})

""")
        
# Add function
def add():
        print("ADD")

        # Have the user input their time log information into the system
        id = int(input("Recorder ID: "))
        month = int(input("Month: "))
        day = int(input("Day: "))
        year = int(input("Year: "))
        time = int(input("Amount of time spent programming (in hours): "))
        aldi = input("Did you work at Aldi? If so, till when? ")
        afton = input("Do you work Afton Alps this afternoon? If so, then when will you leave? ")

        # Take the user input and add it to the database
        cur.execute(f"""INSERT INTO recorder(recorder_id, month, day, year, hours, aldi, afton)
                    VALUES ({id}, {month}, {day}, {year}, {time}, {aldi}, {afton})

        """)
        conn.commit()
    

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
    print("(-99) Quit")

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
    while (entry != -99):
        if (entry == 1):
            add()
        elif (entry == -99):
            break
        
        entry = menu()
    

if __name__ == '__main__':
    main()