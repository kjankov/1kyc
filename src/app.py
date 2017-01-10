from flask import Flask, render_template, request
from datetime import datetime
from onekyc import *

app = Flask(__name__)
app.debug=True

randomuid = ""


@app.route("/")
def home():
	return render_template("index.html")

@app.route("/customer-login")
def login():
	return render_template("login.html")

@app.route("/customer-dashboard", methods=["POST"])
def cdashboard():
	global randomuid
	randomuid = request.form['userid']
	if randomuid != "12345":
		return render_template("customerdashboard_new.html", userid= randomuid)
	return render_template("customerdashboard.html", userid=randomuid)

@app.route("/bank-dashboard")
def bdashboard():

	url2 = "https://blockchain.info/tx/0eae398bccc7b8872142518faa932433bad41e7ca518d4c55afd69841d3fabaf"
	url1 = "https://blockchain.info/tx/0eae398bccc7b8872142518faa932433bad41e7ca518d4c55afd69841d3fabaf"

	return render_template("bankdashboard.html", userid = randomuid, link1 = url1, link2 = url2)


if __name__ == "__main__":
    app.run()
