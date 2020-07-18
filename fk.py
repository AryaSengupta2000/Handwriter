import os
import sqlite3
from flask import Flask,render_template,request
app = Flask(__name__,template_folder='template')

i=0

def convert(filename):
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename) #saves in project directory this needs to be changed to a particular file or db
      return 'file uploaded successfully'

@app.route('/choose',methods = ['GET', 'POST'])
def choose():
    image_names = os.listdir(r'C:\Users\KIIT\Desktop\static\upload')
    return render_template('choose.html', image_names=image_names)

@app.route('/save/<charac>/<paths>')
def save_db(charac,paths):
    print (charac)
    paths = r"C:\Users\KIIT\Desktop\static\upload"+"\\"+paths
    print(paths)
    try:
        sqliteConnection = sqlite3.connect('database.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO alphabets
                                  (alpha, imag) VALUES (?, ?)"""

        empPhoto = convert(paths)
        # Convert data into tuple format
        data_tuple = (charac,empPhoto)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("the sqlite connection is closed")   

    return 'saved'
