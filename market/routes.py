from flask import render_template, request
from pyparsing import nums
from market import my_sql
from market import app
import random


@app.route('/home')
@app.route('/')
def home():
    dict= {
        "Name": "iPhone X",
        "Price": "800",
        "Brand": "Apple",
        # "img" : "./static/photo1.jpeg"
    }
    dict1= {
        "Name": "iPhone 11",
        "Price": "700",
        "Brand": "Samsung",
        # "img" : "./static/photo2.jpeg"
    }
    dict2= {
        "Name": "iPhone 14",
        "Price": "1800",
        "Brand": "Apple",
        # "img" : "./static/photo3.jpeg"
    }
    list =[]
    list.append(dict)
    list.append(dict1)
    list.append(dict2)
    return render_template('home.html',list=list)


@app.route('/customerRegister',methods=['GET','POST'])
def customerRegister():
    if request.method=='POST':
        custDetails = request.form
        First_Name = custDetails['First_Name']
        Last_Name = custDetails['Last_Name']
        Email = custDetails['Email']
        Mobile_No = custDetails['Mobile_No']
        Password = custDetails['Password']
        cur = my_sql.connection.cursor()
        cur.execute("INSERT INTO customer(First_Name,Last_Name,Email,Mobile_No,Password) VALUES(%s, %s, %s, %s, %s)",(First_Name,Last_Name,Email,Mobile_No,Password))
        my_sql.connection.commit()
        cur.close()
    return render_template('customerRegister.html')

@app.route('/adminRegister',methods=['GET','POST'])
def adminRegister():
    if request.method=='POST':
        custDetails = request.form
        First_Name = custDetails['First_Name']
        Last_Name = custDetails['Last_Name']
        Password = custDetails['Password']
        cur = my_sql.connection.cursor()
        cur.execute("INSERT INTO admin(First_Name,Last_Name,Admin_Password) VALUES(%s, %s, %s)",(First_Name,Last_Name,Password))
        my_sql.connection.commit()
        cur.close()
    return render_template('adminRegister.html')

@app.route('/sellerRegister',methods=['GET','POST'])
def sellerRegister():
    if request.method=='POST':
        sellerDetails = request.form
        First_Name = sellerDetails['First_Name']
        Last_Name = sellerDetails['Last_Name']
        Email = sellerDetails['Email']
        Password = sellerDetails['Password']
        Mobile_No = sellerDetails['Phone_Number']
        POO = sellerDetails['Place_Of_Operation']
        cur = my_sql.connection.cursor()
        rand_admin = cur.execute("SELECT Admin_ID FROM admin")
        if rand_admin >0:
            rand_ad = cur.fetchall()
            F_key = random.choice(rand_ad)
            cur.execute("INSERT INTO seller(First_Name,Last_Name,Email,Phone_Number,Password,Place_Of_Operation,Admin_ID) VALUES(%s, %s, %s,%s,%s,%s, %s)",(First_Name,Last_Name,Email,Mobile_No,Password,POO, F_key))
        my_sql.connection.commit()
        cur.close()
    return render_template('sellerRegister.html')