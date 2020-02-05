
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired,ValidationError, Length, Email, EqualTo
from flaskblog.models import User
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed


class RegistrationForm(FlaskForm):
	username = StringField('Username',
							 validators=[DataRequired(),Length(min=2,max=20)])
	email = StringField('Email',
						validators=[DataRequired(),Email()])
	password = PasswordField('Password',
							validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password',
							validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

	def validate_username(self,username):
		user = User.query.filter_by(username = username.data).first()		
		if user:
			raise ValidationError('Username is taken, choose another')
	def validate_email(self,email):
		user = User.query.filter_by(email = email.data).first()		
		if user:
			raise ValidationError('Email is taken, choose another')




class LoginForm(FlaskForm):

	email = StringField('Email',
						validators=[DataRequired(),Email()])
	password = PasswordField('Password',
							validators=[DataRequired()])
	remember = BooleanField('Remember me')
	submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
	username = StringField('Username',
							 validators=[DataRequired(),Length(min=2,max=20)])
	email = StringField('Email',
						validators=[DataRequired(),Email()])
	picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','jgeg','png'])])
	submit = SubmitField('Update')

	def validate_username(self,username):
		if username.data != current_user.username:
			user = User.query.filter_by(username = username.data).first()		
			if user:
				raise ValidationError('Username is taken, choose another')
	def validate_email(self,email):
		if email.data != current_user.email:	
			user = User.query.filter_by(email = email.data).first()		
			if user:
				raise ValidationError('Email is taken, choose another')


class RequestResetForm(FlaskForm):
	email = StringField('Email',
						validators=[DataRequired(),Email()])
	submit = SubmitField('Request Password Reset')

	def validate_email(self,email):
		user = User.query.filter_by(email = email.data).first()		
		if user is None:
			raise ValidationError('There is no Accont with that email. You must register first.')


class ResetPasswordForm(FlaskForm):
	password = PasswordField('Password',
							validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password',
							validators=[DataRequired(), EqualTo('password')])

	submit = SubmitField('Reset Password')