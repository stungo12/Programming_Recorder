# Import SQLite3 to be able to use a database with this program
import sqlite3
# Import Closing from ContextLib to close the database
from contextlib import closing
# Import DateTime to automatically fetch the date
import datetime

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
        # askDate function
        date = askDate()
        monthDate = date[0]
        dayDate = date[1]
        yearDate = date[2]
        time = float(input("Amount of time spent programming (in hours): "))
        aldiWorked = input("Did you work at Aldi? If so, till when? ")
        aftonWorked = input("Do you work Afton Alps this afternoon? If so, then when will you leave? ")

        # Take the user input and add it to the database
        cur.execute(f"""INSERT INTO recorder(recorder_id, month, day, year, hours, aldi, afton)
                    VALUES ({id}, {monthDate}, {dayDate}, {yearDate}, {time}, "{aldiWorked}", "{aftonWorked}");
        
        """)
        # When inputting strings and variables that contain strings, such as aldiWorked and aftonWorked above, into the database
        # they need to be surrounded by quotation marks. So to input a string variable so that it is displayed as a string you 
        # need to do: "{stringVariable}" because just having the curly brackets doesn't work.
        conn.commit()
    
# askDate function
def askDate():
    whenDate = "someday"
    while (whenDate != "today" and whenDate != "yesterday" and whenDate != "manual"):
        whenDate = input("Is the date you wish to enter today's date, yesterday's date, or would you like to manually enter the date (manual)? ")
        # Convert whenDate into all lowercase
    
    # Get the current date using Now()
    current_date = datetime.datetime.now()

    month = 1
    day = 1
    year = 2024

    if (whenDate == "today"):
        print(whenDate)
        # Use Python to find today's date and then split it into month, day, year
        month = current_date.month
        day = current_date.day
        year = current_date.year
        print(f"Today's date is {month}/{day}/{year}")
    elif (whenDate == "yesterday"):
        print(whenDate)
        # Use Python to find yesterday's date and then split it into month, day, year
        month = current_date.month
        day = current_date.day - 1
        year = current_date.year
        print(f"Yesterday's date was {month}/{day}/{year}")
    elif (whenDate == "manual"):
        print(whenDate)
        # Have the user manually input the month, day, year
        month = int(input("Month: "))
        day = int(input("Day: "))
        year = int(input("Year: "))

    date = [month, day, year]
    return date

# View function
def view():
    print("""
          
          
          VIEW
          
          
          """)

    # Query database for it to display all recorded entries
    row = cur.execute("SELECT * FROM recorder;").fetchall()
    print(row)

# Edit function
def edit():
    print("""
          
          
          EDIT
          
          
          """)
    
    # Ask the user what they wish to update
        # This is going to be a bit harder to do and isn't something that I expect to use, so I am going to pass on this for now

# Delete function
def delete():
    print("""
          
          
          Delete
          
          
          """)
    
    # Ask the user what entry they wish to delete based on the Recorder ID
    deleteEntry = int(input("Please enter the Recorder_ID of the entry you would like to delete: "))

    cur.execute(f"""DELETE FROM recorder WHERE recorder_id = {deleteEntry};

""")

# Menu function
def menu():
    print()
    print()    
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
    
    with closing(sqlite3.connect('orders.db')) as conn:
        with closing(conn.cursor()) as cur:
            rows = cur.execute("SELECT 1").fetchall()
            print(rows)
    

if __name__ == '__main__':
    main()