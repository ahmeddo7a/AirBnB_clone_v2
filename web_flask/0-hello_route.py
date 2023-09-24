#!/usr/bin/python3
""" Flask web application
"""
from flask import Flask

#Define the route
@app.route('/', strict_slashes=False)
def hello_flask():
    """Displays Hello HBNB! """
    return "Hello HBNB!"

if __name__ =="__main__":
    #start Server
    app.run(host='0.0.0.0', port=5000)
