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
## Task 3:

# Little lemon needs to know the number of bookings for each table. Please help them to print the table number and the number of bookings for each table.  

# **TIP:** Target `TableNo` column in the booking table, count the number of bookings for each table, and group the data. Print the results in descending order.  
# Add your code here
## Task 4:

# Little lemon wants to create three arrival slots for the guests based on the booking hour: 

# * Late afternoon: for hours 15 and 16  
# * Evening: for hours 17 and 18 
# * Night: for hours 19 and 20 

# Help little lemon to create the above slots and display the booking ID, guest name, and arrival slot on the kitchen screen so that the staff can plan accordingly.  

# **TIP:** Target `GuestFistName` and `GuestLastName` columns and combine them to get `Guest_Name`. Use the MySQL `CASE` function and create `Arrival_slot` for each guest.  
# Add your code here