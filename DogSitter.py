import sqlite3
from flask import Flask, render_template, request
 
app = Flask(__name__)
@app.route("/")
 
def home():
    return render_template("index.html")
 
app.route('Hundevermittlung.html', methods = ['GET','POST'])
def add_Sitter():
 
    if request.method == 'POST':
 
        title = request.form ['name']
 
        price = request.form ['preis']
 
        time = request.form ['zeit']
 
        sittername = request.form ['namehundesitter']
 
        dogowner = request.form ['hundehalter']
 
        age = request.form ['alter']
 
        weight = request.form ['gewicht']
 
        email = request.form ['email']
 
        number = request.form ['nummer']
