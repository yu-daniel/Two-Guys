from flask_wtf import FlaskForm
from wtforms import StringField, DateField, BooleanField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Length

class EmployeeManagerForm(FlaskForm):
	first_name = StringField('First Name', validators=[DataRequired()])
	last_name = StringField('Last Name', validators=[DataRequired()])
	start_date = DateField('Start Date', validators=[DataRequired()])
	status = BooleanField('Vacation', validators=[DataRequired()])
	manager = BooleanField('Manager', validators=[DataRequired()])
	managed_by = StringField('Managed by', validators=[DataRequired()])
	store = StringField('Store', validators=[DataRequired()])
	add = SubmitField('Add Employee/Manager')

class LocationForm(FlaskForm):
	city = StringField('City', validators=[DataRequired()])
	state = StringField('State', validators=[DataRequired()])
	zip_code = DecimalField('Zip Code', validators=[DataRequired()])
	add = SubmitField('Add Location')
