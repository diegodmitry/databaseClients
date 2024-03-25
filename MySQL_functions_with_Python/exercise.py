## C6M3L1 Item 05 – Utilizing MySQL functions using python 

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
# Create cursor object to communicate with entire MySQL database
cursor = connection.cursor()
# Once, the connection is established, and you have a cursor object, you can select the database `little_lemon` and work with the respective table to accomplish the required tasks.  
#cursor.execute("use little_lemon")
# Set little_lemon for use 
cursor.execute("use little_lemon")

# Confirming
connection.database
## Scenario: 

# There are several occasions where Little Lemon needs to perform routine operations, some of them include, total sales, the total number of guests, the number of items in each cuisine, the full name of the guests, and so on. These are only a few examples and writing queries again and again for such routine tasks is not trivial. You can help Little Lemon to handle such tasks using MySQL functions in their python-based application. 
## Task 1:

# Along with the booking ID, little lemon needs to add the full name of the guests in upper case on their invoices. Help little lemon to extract the data in the required format.  

# TIP: Target `GuestFistName`, `GuestLastName` and combine them to get `GuestFullName`.  
# Add your code here
try:
    sql_query_task1 = """
    SELECT BookingID, UPPER(CONCAT(GuestFirstName, ' ', GuestLastName)) AS GuestFullName
    FROM Bookings;
    """

    cursor.execute(sql_query_task1)
    results_task1 = cursor.fetchall()

    print("Guest Full Names in Upper Case:")
    for result in results_task1:
        print("BookingID:", result[0], "GuestFullName:", result[1])

except mysql.connector.Error as e:
    print(e)

## Task 2:

# Little lemon needs to know the following statistics at closing: 

# * Number of bookings 
# * Total sale 
# * Average sale 

# Help little lemon to compute the required statistics from the data in the “Orders” table using python. 

# **TIP:** Target “BookingID” and “BillAmount” columns in the “Orders” table and use MySQL built-in functions to compute the required statistics. Once, you grab the results, use the following python code to print the required output.  

# ```Python
print("Today's statistics:") 
for result in results: 
    print("Number of bookings:",result[0]) 
    print("Total sale:",result[1]) 
    print("Average sale:",result[2]) 
# ```
# Add your code here
try:
    sql_query = """
    SELECT COUNT(DISTINCT BookingID) AS NumberOfBookings, SUM(BillAmount) AS TotalSale, AVG(BillAmount) AS AverageSale
    FROM Orders;
    """

    cursor.execute(sql_query)

    # Fetch and print results
    results = cursor.fetchall()
    print("Today's statistics:") 
    for result in results: 
        print("Number of bookings:", result[0]) 
        print("Total sale:", result[1]) 
        print("Average sale:", result[2])

except mysql.connector.Error as e:
    print(e)

## Task 3:

# Little lemon needs to know the number of bookings for each table. Please help them to print the table number and the number of bookings for each table.  

# **TIP:** Target `TableNo` column in the booking table, count the number of bookings for each table, and group the data. Print the results in descending order.  
# Add your code here
try:
    sql_query_task3 = """
    SELECT TableNo, COUNT(BookingID) AS NumberOfBookings
    FROM Bookings
    GROUP BY TableNo
    ORDER BY NumberOfBookings DESC;
    """

    cursor.execute(sql_query_task3)
    results_task3 = cursor.fetchall()

    # Assuming you want to print the results for Task 3
    print("Number of Bookings for Each Table:")
    for result in results_task3:
        print("TableNo:", result[0], "NumberOfBookings:", result[1])


except mysql.connector.Error as e:
    print(e)

## Task 4:

# Little lemon wants to create three arrival slots for the guests based on the booking hour: 

# * Late afternoon: for hours 15 and 16  
# * Evening: for hours 17 and 18 
# * Night: for hours 19 and 20 

# Help little lemon to create the above slots and display the booking ID, guest name, and arrival slot on the kitchen screen so that the staff can plan accordingly.  

# **TIP:** Target `GuestFistName` and `GuestLastName` columns and combine them to get `Guest_Name`. Use the MySQL `CASE` function and create `Arrival_slot` for each guest.  
# Add your code here
try:
    sql_query_task4 = """
    SELECT BookingID, CONCAT(GuestFirstName, ' ', GuestLastName) AS Guest_Name,
    CASE
        WHEN HOUR(BookingSlot) IN (15, 16) THEN 'Late afternoon'
        WHEN HOUR(BookingSlot) IN (17, 18) THEN 'Evening'
        WHEN HOUR(BookingSlot) IN (19, 20) THEN 'Night'
        ELSE 'Other'
    END AS Arrival_slot
    FROM Bookings;
    """

    cursor.execute(sql_query_task4)
    results_task4 = cursor.fetchall()

    # Print the results for Task 4
    print("Arrival Slots:")
    for result in results_task4:
        print("BookingID:", result[0], "Guest_Name:", result[1], "Arrival_slot:", result[2])

except mysql.connector.Error as e:
    print(e)