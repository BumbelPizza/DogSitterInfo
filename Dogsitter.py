import sqlite3
from flask import Flask, render_template, request, url_for
 
app = Flask(__name__)
@app.route("/")
 
def home():
    return render_template("index.html")
 
app.route('/Hundevermittlung.html', methods = ['GET','POST'])
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
        
        
        print (title)
        print (price)
        print (time)
        print (sittername)
        print (dogowner)
        print (age)
        print (weight)
        print (email)
        print (number)
 
        conn = sqlite3.connect('hunde.db')
 
        cursor = conn.cursor()
 
        cursor.execute(f"INSERT INTO hunde (name, preis, zeit, namehundesitter, hundehalter, alter, gewicht, email, nummer) VALUES ('{title}'), ('{price}'), ('{time}'), ('{sittername}'), ('{dogowner}, ('{age}'), ('{weight}'), ('{email}'), ('{number}')") 
 
        conn.commit()

        conn.close()

        print(f"Name: {title}, Preis: {price}, Zeit: {time}, NameHundeSitter: {sittername}, HundeHalter: {dogowner}, Alter: {age}, Gewicht: {weight}, Email: {email}, Nummer: {number}")
 
         
 
        return "Die Daten wurden erfolgreich übermittelt!"
   
    return render_template("Hundevermittlung.html")
 
if __name__ == '__main__':  
 
    app.run(debug=True)  