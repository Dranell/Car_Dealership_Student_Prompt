#Import MySQL and it's Errors. When there is an error in MySQL we want to see it in PyCharm
import mysql.connector
from mysql.connector import Error

#import your create_data_base.py
import create_data_base as cdb

#Create a function to authenticate your connection to MySQL
def createServerConnection(host_name,user_name,user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password
        )
        print("MySQL Database Connection Successful!")
    except Error as err:
        print(f"Error:{err}")
    return connection

#create a function that will create a database
def create_database(connection,query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        #cursor is created by the connection to mySQL. Think of the cursor as the blinking box ready to be used by the user. We are telling the cursor to
        #execute the query.
        print("Database created successfully!")
    except Error as err:
        print(f"Error: {err}")

#call function to establish connection from main.py to MySQL. Host name will always be localhost. User name is always "root".
#make sure you set the calling of this function equal to 'connection'
connection = createServerConnection("localhost","root","student")
#call function to create Database (this will only be called once. After that we delete it.)
create_database(connection,cdb.create_data_base )