from flask import Flask, render_template, request, url_for, redirect
import json

app = Flask(__name__)

@app.route('/')
def default():
    return redirect(url_for('home'))

@app.route('/home')
def home(register_success=None, login_success=None):
    if register_success is not None and not register_success:
        return render_template('home.html', register_success=False)
    
    elif login_success is not None and not login_success:
        return render_template('home.html', login_success=False)
    else:
        return render_template('home.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['uname']
    password = request.form['pw']
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    success = False
    with open('data.json', 'r+') as f:
        data = json.load(f)
        if username and username not in data.keys() and password and fname and lname and email:
            data[username] = {}
            data[username]['pw'] = password
            data[username]['fname'] = fname
            data[username]['lname'] = lname
            data[username]['email'] = email
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            success = True
    if not success:
        register_success=False
        return home(register_success=False)
    return redirect(url_for('details', username=username, fname=fname, lname=lname, email=email))    

@app.route('/details')
def details():
    return render_template('basic_details.html', 
        username=request.args.get('username'),
        fname=request.args.get('fname'), 
        lname=request.args.get('lname'),
        email=request.args.get('email'))

@app.route('/login', methods=['POST'])
def login():
    # do stuff
    username = request.form['uname']
    password = request.form['pw']
    fname = None
    lname = None
    email = None
    success = False
    with open('data.json', 'r') as f:
        data = json.load(f)
        if username and password and username in data.keys() and data[username]['pw'] == password:
            success = True
            fname = data[username]['fname']
            lname = data[username]['lname']
            email = data[username]['email']

    if not success:
        return home(login_success=False)
    
    return redirect(url_for('details', username=username, fname=fname, lname=lname, email=email))