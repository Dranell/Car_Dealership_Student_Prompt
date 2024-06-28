#Import MySQL and it's Errors. When there is an error in MySQL we want to see it in PyCharm
import mysql.connector
from mysql.connector import Error

#import your create_data_base.py
import create_data_base as cdb

#import your create data table queries
import create_data_table_queries as cdtq

import populate_data_tables_queries as pdtq

import read_data_table_queries as rdtq

#Create a function to authenticate your connection to MySQL
def createServerConnection(host_name,user_name,user_password,db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name
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

#creating a workhorse fuction to execute queries in MySQL
def execute_query(connection,query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful!")
    except Error as err:
        print(f"Error: {err}")

def read_query(connection,query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


#call function to establish connection from main.py to MySQL. Host name will always be localhost. User name is always "root".
#make sure you set the calling of this function equal to 'connection'
connection = createServerConnection("localhost","root","student", "car_dealership")

def displayAllDataTables():
    print("Information for Directory Data Table:")
    directoryDataTable = read_query(connection, rdtq.display_directory_table_information)
    for directoryInformation in directoryDataTable:
        print(directoryInformation)
    print()

    print("Information for Sports Car Data Table:")
    sportsCarDataTable = read_query(connection, rdtq.display_sports_car_table_information)
    for sportsCarInformation in sportsCarDataTable:
        print(sportsCarInformation)
    print()

    print("Information for Sedan Car Data Table")
    sedanCarDataTable = read_query(connection, rdtq.display_sedan_car_table_information)
    for sedanCarInformation in sedanCarDataTable:
        print(sedanCarInformation)
    print()
displayAllDataTables()