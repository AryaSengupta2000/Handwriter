#run this file only once for creating db
import sqlite3

conn = sqlite3.connect('database.db')
print ("Db opened")
conn.execute('CREATE TABLE alphabets (alpha TEXT, imag BLOB)')
print ('table created')
conn.close()