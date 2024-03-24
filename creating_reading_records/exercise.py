## C6M2L1 Item 03 - Creating and reading records
## Generic guidelines     


## Prerequisites  

#To complete this exercise, you must have access to the `“little_lemon”` database. As an authorized user, you need to establish a connection between Python and the database via the connector API and create a `“cursor”` object using the following code: 
import mysql.connector as connector
# Establish connection between Python and MySQL database via connector API
connection=connector.connect(
                            user="root", # use your own
                            password="", # use your own
                            )
# Create cursor object to communicate with entire MySQL database
cursor = connection.cursor()
# Once, the connection is established, and you have a cursor object, you can select the database `“little_lemon”` and print the names of the tables using the following code: 
# Setting little_lemon for use 
cursor.execute("use little_lemon")

# Confirming
print("Database is use is:", connection.database)
print()
print("The existing tables in the little_lemon database are:")
cursor.execute("SHOW TABLES") 
# Print table names 
for table in cursor: 
    print(table)
## Scenario 

# Little Lemon restaurant has created a database and designed tables to keep records of key data. The list of tables that they’ve created are as follows: 

# * A table called `Menu` that stores menu data, 
# * A table called `MenuItems` that stores data on menu items, 
# * A table called `Orders` that stores data on customer orders, 
# * And a table called `Bookings` that stores data on customer bookings. 

# They now need to populate these tables with relevant data. They also need to read the data once the records have been inserted into the database.  

# Help Little Lemon create and read data in their MySQL database using Python. 
## Task 1:

# Insert data in all four tables in the `"little_lemon"` database using Python. Use the following `"INSERT"` queries to populate the tables with relevant data. 

# Use the `"SELECT"` command to check the output and ensure that each `"INSERT"` query has been executed successfully. 
# Add your code here
# Add your code here
try:
    cursor.execute("use little_lemon")
    print(connection.database)
    insert_queries = {
        'MenuItems': """
            INSERT INTO MenuItems (Name, Type, Price) VALUES 
            ('Lemon Chicken', 'Main Course', 20),
            ('Apple Pie', 'Dessert', 10);
        """,
        'Menus': """
            INSERT INTO Menus (MenuID, ItemID, Cuisine) VALUES 
            (1, 1, 'American'),
            (2, 2, 'American');
        """,
        'Bookings': """
            INSERT INTO Bookings (TableNo, GuestFirstName, GuestLastName, BookingSlot, EmployeeID) VALUES 
            (101, 'John', 'Doe', '18:00:00', 1),
            (102, 'Jane', 'Doe', '19:00:00', 2);
        """,
        'Orders': """
            INSERT INTO Orders (OrderID, TableNo, MenuID, BookingID, BillAmount, Quantity) VALUES 
            (1, 101, 1, 1, 40, 2),
            (2, 102, 2, 2, 20, 1);
        """
    }

    for table_name, query in insert_queries.items():
        # print("Insert datas")
        cursor.execute(query)
        
        print(f"Data inserted into {table_name} successfully.")

    # Step 3: Read data from each table to verify
    for table_name in insert_queries.keys():
        # print(table_name)
        cursor.execute(f"SELECT * FROM {table_name};")
        records = cursor.fetchall()
        print(f"\nData from {table_name}:")
        for record in records:
            print(record)

except mysql.connector.Error as e:
    print(e)

## Task 2:

# In the first task, you created records in the empty tables. Now the restaurant requires the following data for each guest: 

# * Guest first and last names  
# * The table number assigned to each guest.  

# You can help Little Lemon to read this data from the “Bookings” table using Python. 

# The SELECT query you need to complete this task is as follows:  

# ```Python
# all_bookings = """SELECT GuestFirstName, GuestLastName, TableNo FROM Bookings;""" 
# ```

# **Tip:** Only read the required columns from the “Bookings” table. Use the  “column_names” attribute from the “cursor” to extract the names of the column and print them using Python’s “print” statement before printing the records. Use for loop to iterate over the “results” that you fetch using the “cursor”. 
# Add your code here
try:
    cursor.execute("use little_lemon")
    print(connection.database)

    # execute SQL query
    all_bookings = """SELECT GuestFirstName, GuestLastName, TableNo FROM Bookings;"""
    cursor.execute(all_bookings)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

except mysql.connector.Error as e:
    print(e)

## Task 3:

# For the next task, you need to read all the records in the `“Menu”` table and retrieve only the first three from the `“cursor”`. Your read query is the following: 

# ```Python
# all_menus = """SELECT * FROM Menus;""" 
# ```

# **Tip:** Explore the functions that you can invoke on the cursor. It is always a good idea to store the query output in a python variable (e.g., “results”) for later use, and you can print them using for loop in python.  

# **Option 1:**
# Add your code here
# After grabbing first three records, the cursor will be at the fourth record and we can call `fetchall()` to grab them.
# Add your code here
# **Options 2:**

# This task can also be accomplished by setting `LIMIT 3` in the `SQL` query.

# Add your code here
try:
    cursor.execute("use little_lemon")
    print(connection.database)

    all_menus = """SELECT * FROM Menus;"""
    cursor.execute(all_menus)

    menus = cursor.fetchmany(3)
    for menu in menus:
        print(menu)

except mysql.connector.Error as e:
    print(e)
    
# Remaining records after fetching the first three
results= cursor.fetchall()
for result in results:
    print(result)
    
# Query to retrieve only first three records from the bookings table is:
all_menus = """SELECT * FROM Menus LIMIT 3;"""

# Execute query 
cursor.execute(all_menus)

# Fetch fist 3 records in results
results = cursor.fetchall()   

# Retrieve column names
cols = cursor.column_names

# Print column names and records from results using for loop
print("""Data in the "Menu" table:""")
print(cols)
for result in results:
    print(result)
    
# Let's close the cursor and the connection
if connection.is_connected():
    cursor.close()
    print("The cursor is closed.")
    connection.close()
    print("MySQL connection is closed.")
else:
    print("Connection is already closed")
