from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, BooleanField, DecimalField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length

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

class IngredientsForm(FlaskForm):
	ingredient_id = IntegerField('Ingredient ID', validators = [DataRequired(), NumberRange(min=1, max=1000)])
	order_date = IntegerField('Order Date', validators = [DataRequired(), NumberRange(min=1, max=10)])
	ingredient_name = StringField('Ingredient Name', validators = [DataRequired(), Length(min=1, max=50)])
	ingredient_cost = IntegerField('Ingredient ID', validators = [DataRequired()])
	order_id = IntegerField('Order ID', validators = [DataRequired(), NumberRange(min=1, max=1000)])
	submit = SubmitField('Submit')
