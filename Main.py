import json
import os
from datetime import datetime,timedelta
from flask import Flask, render_template, request ,redirect,url_for,session,flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename




APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT,r"static\uploads")



# Calling json Config File ##############s
with open('config.json', 'r') as c:
    pramas = json.load(c)['pramas']

app = Flask(__name__)
app.permanent_session_lifetime = timedelta(days=pramas['max_session_day'])
app.config['UPLOAD_FOLDER' ] = UPLOAD_FOLDER
app.secret_key = pramas['s_key']

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
    pin = db.Column(db.Integer,nullable = False)
    dist = db.Column(db.String(20), unique = False , nullable=False)
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
    if 'user' in session :
        return render_template("uindex.html",pramas=pramas,urec = session['name'])
    else:

        return render_template("index.html", pramas=pramas)
# this funsation created becouse for redirece funsatin cant work with blank home
@app.route("/home", methods=['GET'])
def homes():
    if 'user' in session :
        return render_template("uindex.html",pramas=pramas,urec = session['name'])
    else:

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
        
        redirect(url_for('home'))


        
    if 'user' in session:
        return render_template("uContract.html", pramas=pramas,urec= session['name'])
    else:
        return render_template("contract.html", pramas=pramas)





@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("email")
        password = request.form.get("password")
        box = request.form.get("box")        
        record = Users.query.filter_by(email = username , password = password).all()
        count = len(record)
    
        if count == 1 :
            session["user"] = username
            session['pass'] = password
            session['name'] = record[0].name
            session['phone'] = record[0].phone
            session['pin'] = record[0].pin
            session['dist'] = record[0].dist
            
            if str(box) == 'on':
                session.permanent = True
                flash('Login Successfully  Go ahed  ',"success")
                return redirect(url_for('home'))
                
            else:
                session.permanent = False
                flash('Login Successfully , Go ahed :-) ',"success")
                return redirect(url_for('home'))
        else:
            return redirect(url_for("login")) 
    
    elif 'user' in session:
        flash('you are alredy login','info')
        return redirect(url_for('home'))
    else:
        return render_template("login.html", pramas=pramas)





@app.route("/logout")
def logout():

    if 'user' in session :
        session.pop("user",None)
        session.pop("pass",None)
        session.pop("name",None)
        session.pop("phone",None)
        session.pop("pin",None)
        session.pop("dist",None)
        flash('You are successfully logout , see you soon ',"info")
  
        return redirect(url_for('home'))

    else:
        flash('Sorry you are not login yet, So how can You logout',"warning")
        return redirect(url_for('login'))






# ############## For Test ###########
@app.route("/usr")                      #
def Usr():                              #
    if 'user' in session :              #
        return str(session['dist'])     #
    else:                               #
        return "user not found"         #
                                        #
#####################################



@app.route("/registration", methods=['GET', 'POST'])
def registration():
    if (request.method == 'POST'):
        name = request.form.get("name")
        address = request.form.get("address")
        dist = request.form.get("dist")
        pin = request.form.get("pin")
        phone = request.form.get("phone")
        email = request.form.get("email")
        password = request.form.get("pwd")
        cpassword = request.form.get("cpwd")
        con = request.form.get("box")
        # Password Validate or You can say Password Matching  & and Trems condition aprove
        if password == cpassword and str(con) == 'on':
            print("dist === ",dist,"pin -----",pin)
            entry = Users(name=name, address=address, time=datetime.now(
            ), email=email, phone=phone, password=cpassword,dist = dist ,pin = pin)

            db.session.add(entry)
            db.session.commit()
            flash('Thankyou for Registration , Now you can login hare','primary')
            return render_template("login.html", pramas=pramas)
        else:
            flash('ERROR : Plase check you confrim password or accept trams and condition','danger')
            return redirect(url_for('registration'))


    elif 'user' in session:
        flash('you are alredy registration complited','dark')
        return redirect(url_for('home'))
    else:
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

    if 'user' in session :
        flash('Sorry Plase Logout Frist','info')
        return redirect(url_for('home'))
    return render_template("career.html", pramas=pramas)





@app.route("/hire", methods=['GET'])
def hire():
    if 'user' in session:
        emp = Emp.query.filter_by(dist=session['dist']).all()
        return render_template("hire.html", pramas=pramas, len=len(emp), emp=emp)
    else:
        flash("Please Login frist Then You can Access this Future" ,'warning')
        return redirect(url_for('login'))




@app.route('/submenu', methods=['GET'])
def submenu():
    if 'user' in session:
        emp = Emp.query.filter_by(dist=session['dist']).all()
        return render_template("submenu.html", pramas=pramas, len=len(emp), emp=emp)
    else:
        flash("Please Login frist Then You can Access this Future" ,'warning')
        return redirect(url_for('login'))

@app.route('/<name>')
def my_view_func(name):
    if name == "h":
        return "Thankyou"
    return "sorry Page not ablable"
    
if __name__ == '__main__':
    app.run(debug=True)
