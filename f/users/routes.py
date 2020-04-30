from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from f import db, bcrypt
from f.models import User
from f.users.forms import RegistrationForm, LoginForm, UpdateAccountForm

users=Blueprint('users',__name__)

@users.route("/register", methods=['GET', 'POST'])
def register():   ## routes to register
    if current_user.is_authenticated:       ## to check the user authenciated already then redirect it to home page or can be set to login page
        return redirect(url_for('users.home'))
    form = RegistrationForm()        ## RegistrationForm imported from flask 
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') ##password is hashed using the bcrypt
        user = User(username=form.username.data, email=form.email.data, password=hashed_password) ##user data will be saving in the database Usinf the User from model file
        db.session.add(user) 
        db.session.commit()
        flash('now log in')
        return redirect(url_for('users.login')) ##if the entry that was filled in the form is validated it gets return back to the login page for login
    return render_template('register.html', title='Register', form=form) ##otherwise the register page is reloaded 

@users.route("/login", methods=['GET', 'POST'])
def login(): ##routes to login page
    if current_user.is_authenticated: 
        return redirect(url_for('users.account')) ##if the current users is already authenciated then it will be redirected to his/her account page
    form = LoginForm() ##LoginForm imported form Flask
    if form.validate_on_submit(): ##if the user from is validated 
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data): ##password is checked using the chech_password_hash function form bcrypt
            login_user(user)
            next_page = request.args.get('next') ## to get the nest request 
            return redirect(next_page) if next_page else redirect(url_for('users.account'))
        else:
            flash('Login Unsuccess')
    return render_template('login.html', title='Login', form=form) ## if the login is unsucess due to some reason it is reloaded back to login page


@users.route("/logout")
def logout():## route to logout
    logout_user() ##imported form flask
    return redirect(url_for('users.login')) ##redireted to login page

@users.route("/delete",methods=['GET', 'POST'])
@login_required
def delete(): ##to delete the current user
    db.session.delete(current_user) 
    db.session.commit()
    return redirect(url_for('users.login')) ##after deleting the current user it will be redirected to the login page

@users.route("/account", methods=['GET', 'POST'])
@login_required
def account(): ## route to user account page conating information to update the account
    form = UpdateAccountForm() ##imported form flask
    if form.validate_on_submit(): ## it updates the current user data to submitted data obtained from form
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('account.html', title='Account', form=form)