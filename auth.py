import cx_Oracle as cx
from flask import Flask,render_template
import pandas as pd
import config

auth = Flask('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')
