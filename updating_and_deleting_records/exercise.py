## C6M2L1 Item 07 – Updating and deleting records in a MySQL database using Python

## Generic guidelines     

# Refer to the [Exercise](https://www.coursera.org/learn/database-clients/supplement/0oDtw/working-with-labs-in-this-course) for guidance on viewing your code, instructions related to the Jupyter notebook environment, as well as how to access the MySQL database in it.    

## Prerequisite 

# To complete this exercise, you must have access to the `little_lemon` database. As an authorized user, you need to establish a connection between Python and the database via the connector API and create a `cursor` object using the following code:
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
## Scenario 

# Little Lemon restaurant need to update the records of customers in their database. They also need to delete records related to menu items. Let’s see if you can help Little Lemon to complete these update and delete tasks using Python. 
## Task 1:

# The guest Diana Pinto booked a table for two. She was assigned a Booking ID of 6 and the table number 8. However, she just rang Little Lemon to request a change to her booking. She now needs a table for four guests. 

# You need to update Diana’s booking to table 10 in Little Lemon’s MySQL database using Python. Once you have executed the UPDATE query, use the SELECT statement to read all the data from the bookings table and print using for loop to confirm that the booking has been updated.   
# Add your code here


## Task 2: 

# Little Lemon has encountered a conflict with two bookings. To resolve the conflict, you need to update the record for the guest Joakim Iversen, who has a Booking ID of 2.  

# Update Joakim’s booking in the MySQL database using Python as follows: 

# * Change the guest’s table number to 11 
# * Change the `EmployeeID` of the guest’s waiter to 6 

# This guest’s records must be updated in two locations within the booking table.  Once you have executed the code, view the output using a SELECT statement and print using for loop in python. 
# Add your code here


## Task 3: 

# Little Lemon restaurant didn’t receive their regular supply of ingredients today. This means that they can’t provide any Greek cuisine for their guests. They need to delete all Greek cuisine from their menu until the supply of ingredients is restored. 

# Delete these records from the menu table in the Little Lemon database using Python. Once you have executed the code, view the output. 
# Once, the required records are deleted using the above code, you can run the code below to confirm and print the updated "Menus" table.
### Additional on deleting all the records holding NULL values in a certain column.
# **NOTE: Please make sure you have reverted all the changes and your database is in its original state for the upcoming labs.**

# For revisions and learning purpose, you ca recreate the database "little_lemon" and create table and populate them by rerunning the previous labs on:
# * Create your table structure
# * Creating and reading records
# Add your code here