from flask import Flask, jsonify
from flask import request
import json
from Rectangle import Rectangle
from Triangle import Triangle

app = Flask(__name__)

@app.route("/")
def index():
	return "HOLA FLASK"

@app.route("/triangle", methods=["GET", "POST"])
def triangle():
	if request.method == "GET":
		return jsonify({"area":"undefined"})
	elif request.method == "POST":
		amazing = request.json["amazing"]
		height = request.json["height"]
		this_triangle = Triangle(amazing, height)
		area = this_triangle.area()
		return jsonify({"triangle_area":area})

@app.route("/rectangle", methods=["GET", "POST"])
def rectangle():
	if request.method == "GET":
		return jsonify({"area":"undefined"})
	elif request.method == "POST":
		amazing = request.json["amazing"]
		height = request.json["height"]
		this_rectangle = Rectangle(amazing, height)
		area = this_rectangle.area()
		return jsonify({"rectangle_area":area})

@app.route("/triangle-params")
def params():
	amazing = request.args.get('amazing',10)
	height = request.args.get('height',10)
	this_triangle = Triangle(int(amazing), int(height))
	area = this_triangle.area()
	return jsonify({"triangle_area":area})

if __name__ == '__main__':
	app.run(debug = True, port = 5000)