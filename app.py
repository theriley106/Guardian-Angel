from flask import Flask, render_template, request, url_for, redirect, Markup, jsonify, make_response, send_from_directory, session

app = Flask(__name__, static_url_path='/static')

try:
	from keys import *
except:
	API_KEY = raw_input("Key: ")

@app.route('/', methods=['GET'])
def index():
	return render_template("index.html", API_KEY=API_KEY)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
