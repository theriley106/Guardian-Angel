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
	# return render_template("map.html", API_KEY=API_KEY, AGORA_KEY=AGORA_KEY)
	return render_template('index.html', API_KEY = API_KEY)

@app.route('/walker', methods=['GET'])
def select_screen():
	# return render_template("map.html", API_KEY=API_KEY, AGORA_KEY=AGORA_KEY)
	return render_template('walk.html', API_KEY = API_KEY, AGORA_KEY=AGORA_KEY)

@app.route('/gpus', methods=['GET'])
def gpus():
	# return render_template("map.html", API_KEY=API_KEY, AGORA_KEY=AGORA_KEY)
	return render_template('index3.html', API_KEY = API_KEY)

@app.route('/sendText', methods=['GET'])
def send_text():
	# return render_template("map.html", API_KEY=API_KEY, AGORA_KEY=AGORA_KEY)
	message = """Chris has requested a guardian angel to overlook his walk home.  Check out: https://guardianangels.herokuapp.com/mySite?person=Chris&location=Home"""
	os.system("lib messagebird.sms.create --recipient 18646097067 --body {}".format(message))
	return {"status": True}


@app.route('/longLat', methods=['GET'])
def get_long_lat():
	longitude = request.args.get('long')
	latitude = request.args.get('lat')
	print("Long: {} | Lat: {}".format(longitude, latitude))
	longitudeHistory.append(longitude)
	latitudeHistory.append(latitude)
	return jsonify({"status": True})

@app.route('/auth', methods=['GET'])
def auth():
	return "Authentication Successful"

@app.route('/guardian', methods=['GET'])
def get_guardian():
	#print("Long: {} | Lat: {}".format(longitude, latitude))
	longitude = longitudeHistory
	latitude = latitudeHistory
	return render_template("guardian.html", LATITUDE=latitude, LONGITUDE=longitude, AGORA_KEY=AGORA_KEY)

@app.route('/mySite', methods=['GET'])
def my_site():
	#print("Long: {} | Lat: {}".format(longitude, latitude))
	return render_template("mySite.html", API_KEY = API_KEY, AGORA_KEY=AGORA_KEY)

@app.route('/audio', methods=['GET'])
def get_audio():
	return render_template("audio.html", AGORA_KEY=AGORA_KEY)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
