import json
import os
from datetime import datetime

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename




APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT,r"static\uploads")
print("sssssssssssssss0",UPLOAD_FOLDER)


# Calling json Config File ##############s
with open('config.json', 'r') as c:
    pramas = json.load(c)['pramas']

app = Flask(__name__)
app.config['UPLOAD_FOLDER' ] = UPLOAD_FOLDER
print(app.config['UPLOAD_FOLDER'])

# for mail configuration
# app.config.update(
# 	MAIL_SERVER = 'smtp.ga=mail.com',
# 	MAIL_PORT = '465',
# 	MAIL_USE_SSL = True,
# 	MAIL_USERNAME = pramas['email'],
# 	MAIL_PASSWORD = pramas['password']

# )

# mail = Mail(app)


# i adde this line for counter an error
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOAD_FOLDER'] = APP_ROOT

# cheking Uri Type Fron Config.json File
if pramas['local_server'] == 'True':
    app.config['SQLALCHEMY_DATABASE_URI'] = pramas["local_uri"]
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = pramas["pod_uri"]

# SQL Alchemy declear
db = SQLAlchemy(app)


# Fatcch table User From Database
class Users(db.Model):
    time = db.Column(db.String(80), unique=False, nullable=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    address = db.Column(db.String(120), unique=False, nullable=False)
    phone = db.Column(db.String(10), unique=True, nullable=False)
    email = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(20), unique=True, nullable=False)


# fatch contract Table From Data base
class Contract(db.Model):
    sn = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    phone = db.Column(db.String(10), unique=False, nullable=True)
    msg = db.Column(db.String(255), unique=True, nullable=False)


class Emp(db.Model):
    emp_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    phone = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    bio = db.Column(db.String(255), unique=False, nullable=True)
    address = db.Column(db.String(255), unique=False, nullable=False)
    pin = db.Column(db.String(255), unique=False, nullable=False)
    dist = db.Column(db.String(255), unique=False, nullable=False)
    field = db.Column(db.String(255), unique=False, nullable=False)
    ql = db.Column(db.String(255), unique=False, nullable=True)
    cer = db.Column(db.String(255), unique=False, nullable=True)
    exp = db.Column(db.String(255), unique=False, nullable=True)
    adhar_no = db.Column(db.String(255), unique=True, nullable=True)
    adhar_sc = db.Column(db.String(255), unique=False, nullable=False)
    msg = db.Column(db.String(255), unique=False, nullable=True)
    pf = db.Column(db.String(255), unique=False, nullable=False)
    city = db.Column(db.String(255), unique=False, nullable=False)
    state = db.Column(db.String(255), unique=False, nullable=False)


@app.route("/")
def home():
    return render_template("index.html", pramas=pramas)


@app.route("/about")
def about():
    return "sorry page is under devolp"


@app.route("/contract", methods=['GET', 'POST'])
def contract():
    if (request.method == 'POST'):
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        msg = request.form.get("msg")

        entry = Contract(name=name, email=email, phone=phone, msg=msg)

        db.session.add(entry)
        db.session.commit()

        # sendin mail from contract froms
        # mail.send_message("Contract massage form ",
        # 					sender=email,
        # 					recipients = [pramas["email"]],
        # 					body= msg + "\n" + 'my phone :'
        # 					)

        return render_template("/index.html", pramas=pramas)

    return render_template("contract.html", pramas=pramas)


@app.route("/login")
def login():
    return render_template("login.html", pramas=pramas)


@app.route("/registration", methods=['GET', 'POST'])
def registration():
    if (request.method == 'POST'):
        name = request.form.get("name")
        address = request.form.get("address")
        phone = request.form.get("phone")
        email = request.form.get("email")
        password = request.form.get("pwd")
        cpassword = request.form.get("cpwd")
        con = request.form.get("box")
        # Password Validate or You can say Password Matching  & and Trems condition aprove
        if password == cpassword and str(con) == 'on':
            entry = Users(name=name, address=address, time=datetime.now(
            ), email=email, phone=phone, password=cpassword)

            db.session.add(entry)
            db.session.commit()
            return render_template("login.html", pramas=pramas)
        else:
            return str(
                phone) + " Password not Matched <br> or Terms & Conditions not Accepted ,<br> <br><br><a href='registration'> Please Go Back to Registration</a>"

    return render_template("registration.html", pramas=pramas)


@app.route("/career", methods=['GET', 'POST'])
def Career():
    if (request.method == 'POST'):

        name = request.form.get("name")

        pf = request.files["pf"]
        pfpath =os.path.join(UPLOAD_FOLDER, 'emp\profile',secure_filename(name+"_profile_"+pf.filename))
        pf.save(pfpath)

        bio = request.form.get("bio")
        phone = request.form.get("phone")
        email = request.form.get("email")
        address = request.form.get("address")
        city = request.form.get("city")
        dist = request.form.get("dist")
        pin = request.form.get("pin")
        state = request.form.get("state")
        adharno = request.form.get("adharno")

        adharsc = request.files["adharsc"]
        adharpath =os.path.join(UPLOAD_FOLDER, 'emp\\adhar',secure_filename(name+"_adhar_card_"+adharsc.filename))
        pf.save(adharpath)

        field = request.form.get("field")
        ql = request.form.get("ql")

        proof = request.files.getlist("proof")
        proofl = str()
        
        for file in proof:
            key = 0
            path = os.path.join(UPLOAD_FOLDER, 'emp\proofs',secure_filename(name+"_proof_"+email+file.filename))
            file.save(path)
            proofl = proofl +','+ os.path.join(r'static\uploads\emp\proofs',secure_filename(name+"_proof_"+email+file.filename))

        exp = request.form.get("exp")
        msg = request.form.get("msg")
        box = request.form.get("box")

        entry = Emp(name=name, pf=os.path.join(r'static\uploads\emp\profile',secure_filename(name+"_profile_"+pf.filename)), bio=bio, phone=phone, email=email, address=address, city=city, dist=dist,
                    pin=pin, state=state, adhar_no=adharno, adhar_sc=os.path.join(r'static\uploads\emp\\adhar',secure_filename(name+"_adhar_card_"+adharsc.filename)), field=field, ql=ql,
                    cer=proofl, exp=exp, msg=msg)

        db.session.add(entry)
        db.session.commit()
    return render_template("career.html", pramas=pramas)


@app.route("/h", methods=['GET'])
def hire():
    emp = Emp.query.filter_by(dist="North 24 Parganas").all()

    return render_template("hire.html", pramas=pramas, len=len(emp), emp=emp)


app.run(debug=True)
