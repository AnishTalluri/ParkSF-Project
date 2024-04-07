from pymongo import MongoClient

import requests
import json

def add_users_to_db(username,password):

    # Connect to the MongoDB server
    client = MongoClient('mongodb+srv://ychen729:sfhacks@icecreamcluster.t9at9t1.mongodb.net/?retryWrites=true&w=majority&appName=IceCreamCluster')

    # Select the database
    db = client['ParkSF']

    # Select the collection
    collection = db['Users']

    # Data to be inserted
    data = {
        "username": username,
        "password": password
    }

    try:
        # Insert the data into the collection
        result = collection.insert_one(data)
        print("Data inserted successfully with id:", result.inserted_id)
    except Exception as e:
        # Handle errors
        print("Error:", e)
    finally:
        # Close the connection
        client.close()

def verify_user_credentials(username, password):
    # Connect to the MongoDB server
    client = MongoClient('mongodb+srv://ychen729:sfhacks@icecreamcluster.t9at9t1.mongodb.net/?retryWrites=true&w=majority&appName=IceCreamCluster')
    db = client['ParkSF']
    collection = db['Users']

    # Query the database to find the user with the given username and password
    user = collection.find_one({"username": username, "password": password})

    # Close the connection
    client.close()

    # If the user is found, return True; otherwise, return False
    return user is not None

def neurelo_verify_user(username, password):
    url = "https://us-west-2.aws.neurelo.com/rest/Users"
    headers = {"X-API-KEY" : "neurelo_9wKFBp874Z5xFw6ZCfvhXZbJh0Sw2JIKNNVLfkZpU7DAdjDeZv6QTT/qRh5uDjJll5ZYXrxsUJCVIV8+SzODy2k8TXYz9ksFnqIXdS7c0RkaEQjmmyOJ+P5hloiifVRVB2yXVg1C+AB/sktg6F8UptZgBHBM612ZKKERHMkumFIAx7/obyWEd4TWPAAcTxcd_Q9XKz6V2TkM7Aux02q67GhftrLDD8RZXif3Y2jQOuGw="}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data["username"] == username and data["password"] == password:
            return True
    return False

def neurelo_add_user(username, password):
    url = "https://us-west-2.aws.neurelo.com/rest/Users/__one"
    headers = {"X-API-KEY" : "neurelo_9wKFBp874Z5xFw6ZCfvhXZbJh0Sw2JIKNNVLfkZpU7DAdjDeZv6QTT/qRh5uDjJll5ZYXrxsUJCVIV8+SzODy2k8TXYz9ksFnqIXdS7c0RkaEQjmmyOJ+P5hloiifVRVB2yXVg1C+AB/sktg6F8UptZgBHBM612ZKKERHMkumFIAx7/obyWEd4TWPAAcTxcd_Q9XKz6V2TkM7Aux02q67GhftrLDD8RZXif3Y2jQOuGw="}
    
    body = "{ username :" + username + ", password : " + password + "}"

    response = requests.get(url, headers=headers, body=body)
    if response.status_code == 200:
        data = response.json()
        if data["username"] == username:
            return True
    return False