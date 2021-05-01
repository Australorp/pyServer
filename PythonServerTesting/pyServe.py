from flask import Flask, send_from_directory, jsonify, redirect, url_for, request
import json

app = Flask(__name__)

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('../PollApp/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('../PollApp/public', path)

dataFile = open('data.json')
data = dataFile.read()
dataFile.close()

@app.route("/data")
def hello():
    #response = jsonify(data)
    #response.headers.add("Access-Control-Allow-Origin", "*")
    return str(data)

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return ('Hello' + user)
   else:
      user = request.args.get('nm')
      return ('Hello' + user)

#print(data)

if __name__ == "__main__":
    app.run(debug=True)
    #app.run(debug=True, port=4200)
