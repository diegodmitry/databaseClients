# Import MySQL Connector/Python
import mysql.connector as connector
# Establish connection between Python and MySQL database via connector API
connection=connector.connect(
                            user="root",
                            password="",
                            )
## Scenario: 

# Little Lemon needs to perform some basic tasks on its databases such as setting up the database and checking the names of the tables in the database. For this purpose, they have established a connection with the MySQL database using Python. In order to perform a task they need to communicate with the database. 

# You are tasked to help Little Lemon set up their database in use and confirm the existence of tables to perform tasks. This needs to happen according to their requirements in their Python-based application. 
## Task 1
# Little Lemon is restructuring its database and they are interested to know what existing tables are in the database. You need to help them retrieve the names of all the existing tables in their database. 
# To access the names of the existing tables in the Little Lemon database, set the database `little_lemon` in use. Then, create a cursor object and execute `SHOW TABLES` to retrieve the names of the tables in the database. Fetch all the names in a variable and use the `for` loop to print the output.    

# Add your code here

## Task 2

# Creating the cursor is an important step to communicate with the entire MySQL database using Python.  

# You have learned about the different approaches to creating cursors and it depends on your application which approaches you will follow for resource optimization.  

# Run a test between the standard and the buffered cursor to check what type of cursor will work for the situation given below: 

# * Create a cursor 
# * Execute `USE little_lemon` 
# * Execute `SELECT * FROM Bookings` 
# * Execute `SELECT * FROM Orders` 
# Add your code here
## Task 3

# Little Lemon will have multiple databases soon. They need to plan for a scalable solution.  This information can be tracked in a Python dictionary. A dictionary cursor will be helpful as it returns a dictionary object.  

# Create a cursor with argument `[dictionary = True]` and retrieve the names of all the tables in the form of a dictionary object where the name of the tables is a value, and the database name is a key.  

# **TIP:** Explore the arguments that you can pass to the cursor module. 
# Add your code here