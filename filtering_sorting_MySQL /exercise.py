## C6M2L2 Item 03 – Filtering and sorting data
## Prerequisites 

#To complete this exercise, you must have access to the `little_lemon` database. You need to `import MySQL Python/Connector` and, as an authorized user, establish a connection between Python and the MySQL database via connector API using the following code: 
import mysql.connector as connector
# Establish connection b/w Python and MySQL database via connector API
connection=connector.connect(
                            user="root", # use your own
                            password="", # use your own
                            )
# Once, the connection is established, create a `cursor` object to communicate with the entire MySQL database from your python working environment. 
# Create cursor object to communicate with entire MySQL database
cursor = connection.cursor()
# Now, you can select the database `little_lemon` using the code below and work with the respective tables to accomplish the required tasks.  
# Set little_lemon for use 
cursor.execute("use little_lemon")

# Confirm the database in use
connection.database
## Scenario 

# Little Lemon need to filter and sort the data in their MySQL database using Python to complete the following tasks: 

# * Determine which waiter is serving which guest 
# * Identify all guests who paid a bill amount above a certain threshold 
# * And list all starters above a certain price and order with the price. 

# Help Little Lemon extract this data from their database using filtering and sorting techniques. 
## Task 1: 

# Little Lemon need to know how many bookings they have today for table number 12. They also need to know the names of the guests booked for table 12 and who their servers are. 

# Help Little Lemon to complete this task by filtering the records for table 12 from the Bookings table. Show the required records for the following columns in the output: 

# * `TableNo`, 
# * `GuestFirstName`
# * `GuestLastName`
# * `EmployeeID`
# **Exercises**
# Task 1
# The SQL query is:
filtering_and_sorting = """SELECT TableNo, 
GuestFirstName, GuestLastName, EmployeeID  
FROM Bookings 
WHERE TableNo= 12;"""

# Execute query
cursor.execute(filtering_and_sorting)

# Fetch records 
results = cursor.fetchall()

# Retrieve column names
columns = cursor.column_names

# Print column names
print(columns)

# Print query results
for result in results:
    print(result)


## Task 2:

# The SQL query is:
filtering_and_sorting = """SELECT BookingID, BillAmount
FROM
Orders ORDER BY BillAmount DESC;"""

# Execute query
cursor.execute(filtering_and_sorting)

# Fetch records 
results = cursor.fetchmany(size=2)#fetchall()

# Retrieve column names
columns = cursor.column_names

# Print column names
print(columns)

# Print query results
for result in results:
    print(result)

# Little lemon wants to send a coupon to all guests who spent more than $40 at the restaurant today.  

# Help little lemon to filter and sort the records of all quests who qualify for coupon.   


# **TIP:** Target the `BookingID` and `BillAmount` columns in the `Orders` table. Sort the data based on `BillAmount` in `DESC`. 

# Use a fetch module on the cursor or set the limit in your SQL query. 
# Task 2 option 1

## Task 3:
# The SQL query is:
filtering_and_sorting = """SELECT * 
FROM MenuItems 
WHERE (Type = 'Starters' OR Type = 'Desserts')
ORDER BY Price ASC;"""

# Execute query
cursor.execute(filtering_and_sorting)

# Fetch records 
results = cursor.fetchall()

# Retrieve column names
columns = cursor.column_names

# Print column names
print(columns)

# Print query results
for result in results:
    print(result)

# Little lemon needs to determine what the most and least expensive starters and desserts on their menu items are. 

# Help them out by filtering the menu items and sorting them by price using python.  

# **TIP:** Filter the records based on the `Type` column in the `MenuItems` table. Sort the records by `Price` column in `DESC` order. 
# Task 3
