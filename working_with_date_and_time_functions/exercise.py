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
try:
    query = """
    SELECT HOUR(BookingSlot) AS BookingHour, COUNT(BookingID) AS NumberOfBookings
    FROM Bookings
    GROUP BY BookingHour
    ORDER BY BookingHour;
    """
    cursor.execute(query)
    results = cursor.fetchall()

    for (hour, count) in results:
        print(f"Hour: {hour}, Bookings: {count}")

except mysql.connector.Error as e:
    print(e)

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
from datetime import datetime

try:
    query = """
    SELECT TableNo, CONCAT(GuestFirstName, ' ', GuestLastName) AS GuestFullName, BookingSlot
    FROM Bookings
    ORDER BY BookingSlot;
    """
    cursor.execute(query)
    results = cursor.fetchall()

    for (table_no, guest_name, booking_slot) in results:
        booking_time = datetime.strptime(str(booking_slot), '%H:%M:%S')
        print(f"Table {table_no}, Guest: {guest_name}, Arrival Time: {booking_time.hour} hours and {booking_time.minute} mins")

except sql.connector.Error as e:
    print(e)

## Task 3

# A guest with booking ID 2 and table number 12 wants to change the arrival time by one hour. Help Little Lemon to make this change using Python in their application. Use the following steps as a guide to complete this task: 

# * Target `BookingID`, `TableNo` and `BookingSlot` columns in the `Bookings` table.  
# * Add one hour in the “BookingSlot”.  
# * Use the `WHERE` clause on `TableNo` and `BookingID` columns.  
# Add your code here
try:
    booking_id = 2
    table_no = 12

    # SQL to add one hour to the booking slot
    update_query = """
    UPDATE Bookings 
    SET BookingSlot = ADDDATE(BookingSlot, INTERVAL 1 HOUR) 
    WHERE BookingID = %s AND TableNo = %s;
    """
    cursor.execute(update_query, (booking_id, table_no))
    connection.commit()

    print(f"Updated booking slot for booking ID {booking_id} at table {table_no}.")

except mysql.connector.Error as e:
    print(e)