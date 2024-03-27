## C6M3L3 Item 04  - Working with connection pools
## Generic guidelines: 

# Refer to the [Exercise](https://www.coursera.org/learn/database-clients/supplement/0oDtw/working-with-labs-in-this-course) for guidance on viewing your code, instructions related to the Jupyter notebook environment, as well as how to access the MySQL database in it.  

## Prerequisites: 

# To complete this lab, you need to install Python and MySQL. Then you need to install MySQL Connector/Python client or API on your Python environment. Follow the instructions in previous videos to install the required packages or software.  

# To work with MySQL using Python, you must have an authorized user account on the MySQL server.  

## Scenario: 

# Little Lemon’s guests need to access the database for any booking or inquiry, for example, reading the menu. Little Lemon, therefore, needs to establish a connection between the Python and MySQL databases for every operation.  Establishing a connection every time is resource intensive and it is affecting the performance of the Little Lemon application. To improve the performance of the application, Little Lemon needs to establish a pool of database connections to facilitate the guests’ inquiries to the database. 

# You are tasked to help Little Lemon to create a pool of database connections using Python. 
## Task 1

# Create a database connection pool with three connections available for the users to connect. You need to import MySQLConnectionPool class and pass the following arguments: 

# * pool_name = “ll_pool_a” 
# * pool_size = 3 
# * **dbconfig 

# Your database configuration will look like this:  
# ```Python
# dbconfig = { 
#     "database" : "name_of_the_little_lemon_database",  
#     "user" : "your_username", 
#     "password" : "your_password" 
# } 
# ```

# Use the actual name of the database together with authenticated username and password in the above configuration.  

# Please use the Error class from `mysql.connector` to handle the possible error in case the wrong parameters are passed on the database configuration.  

# **Tip:** Use try-except block from Python to implement the error handling. Once the connection pool is created, use the print statements to display the name of the pool and the number of connections in it.  
# Add your code here
import mysql.connector
from mysql.connector.pooling import MySQLConnectionPool

dbconfig = { 
    "database" : "little_lemon",  
    "user" : "root", 
    "password" : "" 
}

try:
    pool = MySQLConnectionPool(pool_name="my_first_pool_conn", pool_size=3, **dbconfig)
    print(f"Connection pool '{pool.pool_name}' is created.")
    print(f"Number of connections in the pool: {pool.pool_size}")

except mysql.connector.Error as e:
    print(e)

## Task 2

# Get a connection from the database connection pool that you have created in the first task and retrieve the following columns from the `Bookings` table: 

# * `BookingID` 
# * `GuestFirstName` 
# * `GuestLastName` 

# Retrieve the required columns and put the connection back into the pool after you have completed the task. 

# **TIP:** Use the `get_connection` module from the `pool` to use the connection. Use `print` statements to display the following message and `close` the connection to return to the pool.  
# Add your code here
import mysql.connector
from mysql.connector.pooling import MySQLConnectionPool

dbconfig = { 
    "database" : "little_lemon",  
    "user" : "root", 
    "password" : "" 
}

try:
    pool = MySQLConnectionPool(pool_name="my_first_pool_conn", pool_size=3, **dbconfig)
    # Get a connection from the pool
    cnx = pool.get_connection()
    print("cnx", cnx)
    cursor = cnx.cursor()
    print("cursor", cursor)
    
    # Define the SQL query to retrieve the specified columns
    query = "SELECT BookingID, GuestFirstName, GuestLastName FROM Bookings"
    
    # Execute the query
    cursor.execute(query)

    # Fetch the results
    for (BookingID, GuestFirstName, GuestLastName) in cursor:
        print(f"BookingID: {BookingID}, GuestFirstName: {GuestFirstName}, GuestLastName: {GuestLastName}")
    
    # Close the cursor and the connection
    # cursor.close()
    # cnx.close()
    # print("The connection is closed and returned to the pool.")
except mysql.connector.Error as e:
    print(f"An error occurred: {e}")

## Task 3

# The following five guests want to connect to the database: 

# * guests = ["Anna", "Marcos", "Diana", "Joakim", "Hiroki"] 

# You only have three connections in the database connection pool. Use the available connection in the `pool` to connect three guests and then add new connections in the pool to connect the remaining two guests. By adding more connection in the pool, make sure that all five guests are connected to the database at the same time.  

# **Tip:** Use `add_connection` module from the `pool` and add a new connection if all are in use. Use `try-except` from Python and print the message to inform the user when connected. 
# Add your code here
import mysql.connector
from mysql.connector.pooling import MySQLConnectionPool

dbconfig = { 
    "database" : "little_lemon",  
    "user" : "root", 
    "password" : "" 
}

guests = ["Anna", "Marcos", "Diana", "Joakim", "Hiroki"]
connected_guests = []

try:
    # Attempt to connect each guest
    for guest in guests:
        try:
            pool = MySQLConnectionPool(pool_name="my_first_pool_conn", pool_size=3, **dbconfig)
            # Try to get a connection from the pool
            connection = pool.get_connection()
            print(f"{guest} is connected to the database.")
            connected_guests.append(guest)
            connection.close()
        except mysql.connector.errors.PoolError:
            # If no connection is available, increase the pool size and retry
            new_pool_size = len(connected_guests) + 1  # Increase the pool by one for simplicity
            pool = MySQLConnectionPool(pool_name="ll_pool_a", pool_size=new_pool_size, **dbconfig)
            print(f"Pool size increased to {new_pool_size}. Retrying connection for {guest}...")
            connection = pool.get_connection()  # Retry getting a connection
            print(f"{guest} is connected to the database.")
            connected_guests.append(guest)
            connection.close()
except mysql.connector.Error as e:
    print(f"An error occurred: {e}")