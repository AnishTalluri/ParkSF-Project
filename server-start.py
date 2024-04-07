import http.server
import socketserver

from flask import Flask, render_template, request
import requests

# Define the port you want the server to listen on
PORT = 8000

# Define the directory path you want to serve files from
DIRECTORY = ""

# Change the current working directory to the specified directory
# This is necessary because SimpleHTTPRequestHandler serves files relative to the current directory
import os
#os.chdir(DIRECTORY)


# Create a TCP server
#with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
    #print("Server started at port", PORT)
    
    # Start serving requests indefinitely
    #httpd.serve_forever()

app = Flask("parkSF")

@app.route(r'/users')
def get_faciltiies():
    url = "https://osp.cit.cc.api.here.com/parking/segments?bbox=41.389405513925354,2.127549994463742,41.38042236108416,2.139522979169079&geometryType=tpegOpenLR&geometryType=segmentAnchor"
    api_key = request.args.get('api_key')
    headers = {'Authorization' : 'Bearer ' + api_key}
    response = requests.get(url, headers=headers)
    print(response.status_code)
    #print(response)
    return str(response.status_code)

@app.route(r'/')
def get_main():
    return render_template("main.html")

@app.route(r'/login.html')
def get_login():
    return render_template("login.html")

@app.route(r'/register.html')
def get_register():
    return render_template("register.html")

@app.route(r'/login2.html')
def get_login2():
    return render_template("login2.html")

@app.route(r'/main.html')
def get_logout():
    return render_template("main.html")

app.run(debug=True)