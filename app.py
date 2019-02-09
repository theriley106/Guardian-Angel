from flask import Flask, render_template, request, url_for, redirect, Markup, jsonify, make_response, send_from_directory, session
import os
is_prod = os.environ.get('IS_HEROKU', None)

if is_prod == None:
	try:
		from keys import *
	except:
		API_KEY = input("Key: ")
		FIREBASE_KEY = input("Firebase Key: ")
else:
	API_KEY = os.environ.get('GOOGLE_KEY', None)

app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=['GET'])
def index():
	return render_template("index.html", API_KEY=API_KEY)

@app.route('/firebase', methods=['GET'])
def index_firebase():
	return render_template("gcp.html", FIREBASE_KEY=FIREBASE_KEY)

@app.route('/longLat', methods=['GET'])
def get_long_lat():
	longitude = request.args.get('long')
	latitude = request.args.get('lat')
	print("Long: {} | Lat: {}".format(longitude, latitude))
	return jsonify({"status": True})


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
