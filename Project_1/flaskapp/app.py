from flask import Flask, render_template, request

application = Flask(__name__)

@application.route('/')
def home():
    return render_template('home.html')

@application.route("/update_details")
def hello_world():
    return render_template('basic_details.html')

@application.route('/submit_data', methods=['POST'])
def submit_data():
    # do stuff
    data = "Data Updated! \n" \
        f"New first name: {request.form['fname']}\n" \
        f"New last name: {request.form['lname']}"
    return data