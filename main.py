#Import MySQL and it's Errors. When there is an error in MySQL we want to see it in PyCharm
import mysql.connector
from mysql.connector import Error

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
#call function to establish connection from main.py to MySQL. Host name will always be localhost. User name is always "root".
createServerConnection("localhost","root","student")