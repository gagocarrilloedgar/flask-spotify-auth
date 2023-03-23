import json
from flask import Flask, request, redirect, g, render_template, jsonify
import requests
from urllib.parse import quote
from auth import SpotifyAPI


# Here you need to add your client secret and ID
CLIENT_ID = ""
CLIENT_SECRET = ""


## Create flask app
app = Flask(__name__)


## Create spotify api instance
api = SpotifyAPI(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)


@app.route("/track/<string:id>")
def index(id):
    print(id)
    # Auth Step 1: Authorization
    token = api.get_access_token()
    track = api.get_track(id)

    return jsonify({"track": track})


if __name__ == "__main__":
    app.run(debug=True, port=3001)
