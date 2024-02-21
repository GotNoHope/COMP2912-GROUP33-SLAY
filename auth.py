#for login, logout, signup

from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #logic for verifying login details
        return redirect(url_for('main.home'))
    return render_template('login.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        #logic for registering new user details
        return redirect(url_for('auth.login'))
    return render_template('signup.html')

@auth.route('/logout', methods=['GET', 'POST'])
def signup():
    #logic for logging out user
    return render_template(url_for('main.home'))


