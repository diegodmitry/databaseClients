## C6M3L2 Item 04 – Stored procedures using python

## Generic guidelines: 

# Refer to the [Exercise](https://www.coursera.org/learn/database-clients/supplement/0oDtw/working-with-labs-in-this-course) for guidance on viewing your code, instructions related to the Jupyter notebook environment, as well as how to access the MySQL database in it.  

## Prerequisites: 

# To complete this exercise, you must have access to the `little_lemon` database. As an authorized user, you need to establish a connection between Python and the database via the MySQL Connector/Python API and create a `cursor` object using the following code: 
import mysql.connector as connector
# Establish connection b/w Python and MySQL database via connector API
connection=connector.connect(
                            user="root", # use your own
                            password="", # use your own
                            )
# Create a cursor object to communicate with entire MySQL database
cursor = connection.cursor()
# Once, the connection is established, and you have a cursor object, you can select the database `little_lemon` using the code below and work with the respective table to accomplish the required tasks. 
# Set the little_lemon database for use 
cursor.execute("use little_lemon")

# Confirm the database in use
connection.database
## Scenario: 

# Little lemon need to perform some tasks on daily basis, and they involve extracting data from one or more tables. The tasks include finding the guest with maximum spending, retrieving the bookings for no arrival, and displaying the order status to the guests. To keep consistency during the data retrieval process, Little Lemon is interested to implement the required tasks using stored procedures. You can help Little Lemon and create stored procedures so that they can call them according to their requirements in their python-based application. 
## Task 1:

# Little lemon is running a marketing campaign this month. They need to issue a discount coupon to the top spender on daily bases. Create a stored procedure `TopSpender` that can retrieve the booking ID, guest’s full name, and the bill amount of the top spender at closing. Call the procedure and print the results.   

# **TIP:** Target `BookingID`, `GusetFistName`, `GuestLastName` and `BillAmount` columns from the `Bookings` and the `Orders` tables. Use the concatenation function to get the guest’s full name. Join the two tables and retrieve the top spender. Create a stored procedure, call it by its name using python and print the results. 
cursor.execute("DROP PROCEDURE IF EXISTS TopSpender;")
stored_procedure_query="""
CREATE PROCEDURE TopSpender()

BEGIN

SELECT bookings.BookingID, 
CONCAT(
bookings.GuestFirstname,
' ',
bookings.GuestLastname
) AS CustomerName,
Orders.BillAmount 
FROM Bookings
INNER JOIN
Orders ON bookings.BookingID=Orders.BookingID
ORDER BY BillAmount DESC LIMIT 1;

END

"""

# Execute the query
cursor.execute(stored_procedure_query)

#********************************************#

# Call the stored procedure with its name
cursor.callproc("TopSpender")

# Retrieve recrods in "dataset"
results = next( cursor.stored_results() )
dataset = results.fetchall()

# Retrieve column names using list comprehension in a 'for' loop 
for column_id in cursor.stored_results():
    columns = [ column[0] for column in column_id.description ]

# Print column names
print(columns)

# Print data 
for data in dataset:
    print(data)

## Task 2:

# Help Little Lemon to retrieve all those bookings where the guests did not appear today. How will you implement this task using a stored procedure? Use `NoArrival` as a name for your stored procedure.  

# TIP: Target the `Orders` and the `Bookings` tables, join them on `BookingID` and retrieve the records with a `NULL` value in the bill amount. Create a stored procedure, call it by its name using python and print the results.
cursor.execute("DROP PROCEDURE IF EXISTS NoArrival;")
stored_procedure_query="""
CREATE PROCEDURE NoArrival()

BEGIN

SELECT bookings.BookingID, 
Orders.BillAmount 
FROM Bookings
LEFT JOIN
Orders ON Bookings.BookingID=Orders.BookingID
WHERE BillAmount IS NULL;

END

"""

# Execute the query 
cursor.execute(stored_procedure_query)

#********************************************#

# Call the stored procedure with its name
cursor.callproc("NoArrival")

# Retrieve recrods in "dataset"
results = next( cursor.stored_results() )
dataset = results.fetchall()

# Retrieve column names using list comprehension in a 'for' loop 
for column_id in cursor.stored_results():
    columns = [ column[0] for column in column_id.description ]

# Print column names
print(columns)

# Print data 
for data in dataset:
    print(data)

## Task 3:

# It is very important for little lemon to keep track of the status of each guest’s order and display it on the screen to keep their guests informed.  

# This is how they categorize the orders: 

# * If not assigned to any employee, the status is `In Queue` 
# * If assigned to the employees with IDs 4 and 5, the status is `Preparing Order` 
# * If assigned to the employees with IDs 1, 2, and 3, the status is `Order Served` 

# Create a stored procedure named `OrderStatus` for the above task and call to check if everything is working.  

# **TIP:** Target `EmployeeID` column in the `Bookings` table and use the `CASE` function in your stored procedure query. Create a stored procedure, call it by its name using python and print the results.  
cursor.execute("DROP PROCEDURE IF EXISTS OrderStatus;")

stored_procedure_query="""
CREATE PROCEDURE OrderStatus()

BEGIN

SELECT bookingID, 
CASE
WHEN employeeID IN (1,2,3) THEN "Order Served" 
WHEN employeeID IN (4,5) THEN "Preparing Order" 
ELSE "In Queue" 
END AS Status
FROM Bookings;

END

"""

# Execute the query
cursor.execute(stored_procedure_query)

#********************************************#

# Call the stored procedure with its name
cursor.callproc("OrderStatus")

# Retrieve recrods in "dataset"
results = next( cursor.stored_results() )
dataset = results.fetchall()

# Retrieve column names using list comprehension in a 'for' loop 
for column_id in cursor.stored_results():
    columns = [ column[0] for column in column_id.description ]

# Print column names
print(columns)

# Print data 
for data in dataset:
    print(data)