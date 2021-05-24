from flask import Flask, render_template, request, redirect, url_for, logging, session, flash, make_response
from datetime import date, time, datetime
import yfinance as yf
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from wtforms import  BooleanField, PasswordField, StringField
from wtforms.validators import InputRequired, Email, Length
#import matplotlib.pyplot as plt
#import mplfinance as fplt
import numpy as np
import pandas as pd
import requests


#from passlib.hash import sha256_crypt

app = Flask(__name__)

app.secret_key='Not Verified'
# the database

@app.route("/")
def index():
	sg ='EURUSD=X'
	data= yf.Ticker(sg)
	dataDF= data.history(period='1m', start='2020-1-1', end='3000-01-01')
   
	return render_template('index.html', data =dataDF)
@app.route("/SMA")
def SMA():
	return render_template('SMA.html')
@app.route("/EMA")
def EMA():
	return render_template('EMA.html')
@app.route("/MACD")
def MACD():
	return render_template('MACD.html')
@app.route("/RSI")
def RSI():
	return render_template('RSI.html')
@app.route("/candlstick")
def candlstick():
	return render_template('candlstick.html')
@app.route("/Bollinger")
def Bollinger():
	return render_template('Bollinger.html')
@app.route("/lineaire")
def lineaire():
	return render_template('lineaire.html')
#login form

if __name__=="__main__":
	app.run()
