from flask import Flask,render_template,request
app = Flask(__name__)

i=0


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
    global i
    while i <=48 :
        i+=1
        return render_template('choose.html',i=i)