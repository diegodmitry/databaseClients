## C6M3L1 Item 09 - Date and time using Python
## Generic guidelines: 

# Refer to the [Exercise](https://www.coursera.org/learn/database-clients/supplement/0oDtw/working-with-labs-in-this-course) for guidance on viewing your code, instructions related to the Jupyter notebook environment, as well as how to access the MySQL database in it. 

## Prerequisites: 

# To complete this lab, you must have access to the `little_lemon` database. As an authorized user, you need to establish a connection between Python and the database via the MySQL Connector/Python API and create a `cursor` object using the following code: 
import mysql.connector as connector
# Establish connection between Python and MySQL database via MySQL Connector/Python API
connection=connector.connect(
                            user="root",
                            password="",
                            )
# Create cursor object to communicate with entire MySQL database
cursor = connection.cursor()
# Once the connection is established and you have a cursor object, you can select the database `little_lemon` using the code below and work with the respective table to complete the required tasks.  
# Set the little_lemon database for use 
cursor.execute("use little_lemon")

# Confirm the datbase in use
# connection.database
## Scenario: 

# Little Lemon needs to schedule its staff’s duties according to the restaurant’s peak hours. They also want to display the guest’s name and their expected arrival time kitchen screen to keep the staff informed. These and several other similar tasks, such as changing the booking time, require working with the date and time column.  

# You are tasked to help Little Lemon work with the date and time columns using Python for their Python-based application. 
## Task 1

# Little Lemon wants to retrieve the number of bookings in each hour so that they can schedule the staff duties accordingly. Use the following steps as a guide to complete this task:  

# * Target the “BookingID” and “BookingSlot” columns from the “Bookings” table.  
# * Extract the hour from the “BookingSlot” column and count the bookings in each hour. 
# * Group and order the data by hour.  

# **TIP:** Use MySQL `HOUR`, `COUNT`, `GROUP BY` and `ORDER BY` to accomplish the task. 
# Add your code here
## Task 2

# Little Lemon needs to display the following information in the staff’s room: 

# * Table number 
# * Guest’s full name 
# * Arrival time in hours and minutes (e.g., 15 hours and 0 mins) 

# Help Little Lemon to retrieve and display the required information. Use the following steps as a guide to complete this task: 

# * Target `TableNo`, `GuestFirstName`, `GuestLastName` and `BookingSlot` columns in the `Bookings` table.  
# * Order the data by `BookingSlot`.  
# * Use Python’s `datetime` module to extract hours and minutes using the `strptime` function when printing the record.  
# Add your code here
## Task 3

# A guest with booking ID 2 and table number 12 wants to change the arrival time by one hour. Help Little Lemon to make this change using Python in their application. Use the following steps as a guide to complete this task: 

# * Target `BookingID`, `TableNo` and `BookingSlot` columns in the `Bookings` table.  
# * Add one hour in the “BookingSlot”.  
# * Use the `WHERE` clause on `TableNo` and `BookingID` columns.  
# Add your code here