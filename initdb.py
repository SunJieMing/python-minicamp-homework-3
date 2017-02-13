import sqlite3

connection = sqlite3.connect('database.db')
print "Opened database successfully";

connection.execute('CREATE TABLE foods (name TEXT, calories TEXT, cuisine TEXT, is_vegetarian TEXT, is_gluten_free TEXT)')
print "Table created successfully";
connection.close()
