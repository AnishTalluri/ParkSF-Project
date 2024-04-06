import http.server
import socketserver

# Define the port you want the server to listen on
PORT = 8000

# Define the directory path you want to serve files from
DIRECTORY = "/path/to/your/directory"

# Change the current working directory to the specified directory
# This is necessary because SimpleHTTPRequestHandler serves files relative to the current directory
import os
os.chdir(DIRECTORY)


# Create a TCP server
with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
    print("Server started at port", PORT)
    
    # Start serving requests indefinitely
    httpd.serve_forever()

@app.route('\users')
def get_faciltiies():
    api_key = request.args.get('api_key')
    headers = {'Authorization' : 'Bearer ' + api_key}
    response = requests.get(url, headers=headers)
    print(response)