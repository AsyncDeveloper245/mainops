from flask import Flask, render_template, redirect, url_for, request,current_app,g
import requests
from pymongo import MongoClient
import base64
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app)
client = MongoClient('localhost', 27017)
FRONTEND_SERVER_URL = "http://localhost:3000"

db = client.credentials_db
credentials = db.credentials


@app.route("/",methods=["POST","GET"])
def add_content(identifier=None):
    if request.method == "POST":

        creds = json.loads(request.data)
        key = creds.get("key")
        encoded_value = base64.b64encode(key.encode('utf-8'))
        print(encoded_value)
        credentials.insert_one({"key":key,"encoded_value":encoded_value})
        print(credentials.find_one({"key":key}))
        return json.dumps({"status":"success","encoded-value":str(encoded_value)})
    # if request.method == "GET":
    #     credentials.find_one({"identifier":identifier})

@app.route("/credentials/list",methods=["GET"])
def list_content(credential_key):
    if request.method == "GET":
        credentials = mongo.db.myCollection.find(credential_key)
        requests.post(FRONTEND_SERVER_URL, json=credentials)

if __name__ == "__main__":
    app.run(debug=True)