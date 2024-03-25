## C6M2L2 Item 07 – Performing different JOIN operations in MySQL database using python 

## Generic guidelines: 

# Refer to the [Exercise](https://www.coursera.org/learn/database-clients/supplement/0oDtw/working-with-labs-in-this-course) for guidance on viewing your code, instructions related to the Jupyter notebook environment, as well as how to access the MySQL database in it. 
 

## Prerequisites 

# To complete this exercise, you must have access to the `little_lemon` database. You need to import MySQL Python/Connector and, as an authorized user, establish a connection between Python and the MySQL database via connector API using the following code: 
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
# Set little_lemon database for use 
cursor.execute("use little_lemon")

# Confirm the database in use
connection.database
## Scenario 

# Little Lemon needs to carry out the following tasks with their datasets: 

# * Determine the final bill amount for each customer who attended the restaurant today 
# * Identify the type of cuisine that each item in their menu belongs to. 

# Help Little Lemon to complete these tasks using “JOIN” operations on the restaurant’s MySQL database using Python. 
## Task 1:

# Little Lemon need the following information for each of the items in their menu: 

# * The name of each item in the menu, 
# * Each menu item’s type, 
# * Each menu item’s cuisine, 
# * and the price of each item in the menu. 

# Help Little Lemon to extract this data from their database using Python. 

# **TIP:** You need to combine records from the `MenuItems` and `Menu` tables using the `JOIN` operation and show only the requested columns in the output. 
# Add your code here
## Task 2:

# Little Lemon notice that there are several menu items missing from the output of the previous task. 

# Help Little Lemon to identify these missing items by using a `JOIN` operation in Python to return data for the missing records. 

# **TIP:** Use a `JOIN` operation to return the missing data by joining the `MenuItems` and Menu tables. 
# Add your code here
## Task 3:

# Little Lemon restaurant need you to help them retrieve the following information from the `Bookings` and the `Orders` tables in their MySQL database using Python: 

# * Booking ID 
# * Table number 
# * Guest first name 
# * Server ID 
# * Bill amount  

# **TIP:** Combine the records from the `Bookings` and the `Orders` tables using a `JOIN` operation. The requested column `ServerID` is the `EmployeeID` column in the `Booking` table. Create an alias for this purpose.  
# Add your code here