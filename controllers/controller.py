from app import app
from flask import render_template
from modules.calculator import *

@app.route('/')
def index():
    return "Hello"

@app.route('/add/<num_1>/<num_2>')
def add(num_1, num_2):
    calculation = addition(int(num_1), int(num_2))
    return render_template('index.html', title="Addition", output=calculation)

@app.route('/sub/<num_1>/<num_2>')
def sub(num_1, num_2):
    calculation = subtraction(int(num_1), int(num_2))
    return render_template('index.html', title="Subtraction", output=calculation)

@app.route('/mult/<num_1>/<num_2>')
def mult(num_1, num_2):
    calculation = multiplication(int(num_1), int(num_2))
    return render_template('index.html', title="Multiplication", output=calculation)

@app.route('/div/<num_1>/<num_2>')
def div(num_1, num_2):
    calculation = division(int(num_1), int(num_2))
    return render_template('index.html', title="Division", output=calculation)

