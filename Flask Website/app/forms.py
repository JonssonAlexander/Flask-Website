
from ast import Sub
from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length 
from app.models import User

class LoginForm(FlaskForm):
    username=StringField('Username', validators=[DataRequired()]) #Vad betyder [DataRequired]?
    password=PasswordField('Password', validators=[DataRequired()])
    remember_me=BooleanField('Remember me')
    submit=SubmitField('Sign in')

class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    email=StringField('Email', validators=[DataRequired(), Email()]) #Fungerar men kräver att man skriver in en mail med @, annars kan man inte skapa ett konto och den registreras inte i databasen.
    password=PasswordField('Password', validators=[DataRequired ()])
    password2=PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit=SubmitField('Register')
    
    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('This username is taken. Please use another username.')
    
    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('This email is already taken. Please use another email.')

class EditProfileForm(FlaskForm):
    username= StringField('Username', validators=[DataRequired()])
    about_me= TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit=SubmitField('Register')
    
    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username=original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user= User.query.filter_by(username=self.username).first()
            if user is not None: 
                raise(ValidationError('Please use a different username'))

class EmptyForm(FlaskForm):
    submit=SubmitField('Submit')

class PostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ResetPasswordRequestForm(FlaskForm):
    email=StringField('email', validators=[DataRequired(), Email()])
    submit= SubmitField('Request password reset')

class ResetPasswordForm(FlaskForm):
    password=PasswordField('Password', validators=[DataRequired()])
    password2=PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit=SubmitField('Request Password Reset')


