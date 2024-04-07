from pymongo import MongoClient

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