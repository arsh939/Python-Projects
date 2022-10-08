# importing required libraries
import mysql.connector
 
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="user",
  passwd ="root"
)
 
# preparing a cursor object
cursorObject = dataBase.cursor()
 
# creating database named studentdatabase
cursorObject.execute("CREATE DATABASE studentdatabase")

