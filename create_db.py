import mysql.connector

#declare your database variables
DBHOST = 'localhost'
DBUSER = 'root'
DBPASS = '' 

#establish the connection
connection = mysql.connector.connect(host=DBHOST, user=DBUSER, passwd=DBPASS)

my_cur = connection.cursor()
my_cur.execute("DROP DATABASE IF EXISTS FlaskApp")
my_cur.execute("CREATE DATABASE if not exists FlaskApp")
my_cur.execute("USE FlaskApp")
my_cur.execute("CREATE TABLE Data (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), phone VARCHAR(255))")