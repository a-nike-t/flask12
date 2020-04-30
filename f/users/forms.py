from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField ##different types of field that form will contains
from wtforms.validators import DataRequired, Length, Email, ValidationError ## data required so that it is compulsory to fill that field
from flask_login import current_user ## to get  the current user
from f.models import User## users that was created in models

class RegistrationForm(FlaskForm): ## registeration form 
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username): ## if username validation is unsuccessfull it will return Validation Error 
        user = User.query.filter_by(username=username.data).first() ## it will check the entered username exists or not
        if user:
            raise ValidationError('username exist')

    def validate_email(self, email): ## if username validation is unsuccessfull it will return Validation Error 
        user = User.query.filter_by(email=email.data).first() ## it will check the entered email exists or not
        if user:
            raise ValidationError('email exist')


class LoginForm(FlaskForm): ## login form 
    username = StringField('Username',
                        validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm): ## to update account details
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Update')

    def validate_username(self, username): ## validate useraname 
        ## same as the above mentioned validate_username in Registeration Form we can use that also with the decorator
        ##having extra functionality fron checking the current user condition
        if username.data != current_user.username:      
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken')

    def validate_email(self, email):
        ## same as the above mentioned validate_email in Registeration Form we can use that also with the decorator
        ##having extra functionality fron checking the current user condition
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken')