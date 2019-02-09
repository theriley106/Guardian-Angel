from flask import Flask, render_template, request, url_for, redirect, Markup, jsonify, make_response, send_from_directory, session
import os
is_prod = os.environ.get('IS_HEROKU', None)
longitudeHistory = [None]
latitudeHistory = [None]
if is_prod == None:
	from keys import *
else:
	API_KEY = os.environ.get('GOOGLE_KEY', None)
	AGORA_KEY = os.environ.get('AGORA_KEY', None)
	FIREBASE_KEY = os.environ.get('FIREBASE_KEY', None)

app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=['GET'])
def index():
	return render_template("map.html", API_KEY=API_KEY, AGORA_KEY=AGORA_KEY)

@app.route('/longLat', methods=['GET'])
def get_long_lat():
	longitude = request.args.get('long')
	latitude = request.args.get('lat')
	print("Long: {} | Lat: {}".format(longitude, latitude))
	longitudeHistory.append(longitude)
	latitudeHistory.append(latitude)
	return jsonify({"status": True})

@app.route('/guardian', methods=['GET'])
def get_guardian():
	#print("Long: {} | Lat: {}".format(longitude, latitude))
	longitude = longitudeHistory
	latitude = latitudeHistory
	return render_template("guardian.html", LATITUDE=latitude, LONGITUDE=longitude, AGORA_KEY=AGORA_KEY)

@app.route('/mySite', methods=['GET'])
def my_site():
	#print("Long: {} | Lat: {}".format(longitude, latitude))
	return render_template("mySite.html")

@app.route('/audio', methods=['GET'])
def get_audio():
	return render_template("audio.html", AGORA_KEY=AGORA_KEY)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
