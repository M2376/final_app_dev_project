# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import outcome

app = Flask(__name__)
# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/results', methods=['GET','POST'])
def results():
    if request.method == 'POST':
        print(request.form)
        user_Markers= request.form["Markers"]
        user_Scissors = request.form["Scissors"]
        user_Pillows = request.form["Pillows"]
        user_Wood = request.form["Wood"]
        outcome_info = outcome(user_Markers,user_Scissors,user_Pillows,user_Wood)
        return render_template('results.html', outcome_info=outcome_info)
    else:
        return "error"

