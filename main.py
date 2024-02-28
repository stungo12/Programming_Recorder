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
        
# Add function
def add():
        print("""
          
          
          ADD
          
          
          """)

        # Have the user input their time log information into the system
        id = int(input("Recorder ID: "))
        monthDate = int(input("Month: "))
        dayDate = int(input("Day: "))
        yearDate = int(input("Year: "))
        time = float(input("Amount of time spent programming (in hours): "))
        aldiWorked = input("Did you work at Aldi? If so, till when? ")
        aftonWorked = input("Do you work Afton Alps this afternoon? If so, then when will you leave? ")

        # Take the user input and add it to the database
        cur.execute(f"""INSERT INTO recorder(recorder_id, month, day, year, hours, aldi, afton)
                    VALUES ({id}, {monthDate}, {dayDate}, {yearDate}, {time}, "{aldiWorked}", "{aftonWorked}");

        """)
        conn.commit()
    

# View function
def view():
    print("""
          
          
          VIEW
          
          
          """)

    # Query database for it to display all recorded entries
    print(cur.execute("SELECT * FROM recorder;").fetchall())

# Edit function
def edit():
    print("""
          
          
          EDIT
          
          
          """)

# Delete function
def delete():
    print("""
          
          
          Delete
          
          
          """)

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
        elif (entry == 2):
            view()
        elif (entry == 3):
            edit()
        elif (entry == 4):
            delete()
        elif (entry == -99):
            break
        else:
            print("Wrong entry, please try again")
        
        entry = menu()
    

if __name__ == '__main__':
    main()