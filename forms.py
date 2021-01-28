from flask_wtf import FlaskForm
from wtforms import StringField, DateField, BooleanField, DecimalField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange


class EmployeeManagerForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), NumberRange(min=1, max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), NumberRange(min=1, max=50)])
    start_date = DateField('Start Date', validators=[DataRequired()])
    status = BooleanField('Vacation', validators=[DataRequired()])
    manager = BooleanField('Manager', validators=[DataRequired()])
    managed_by = StringField('Managed by', validators=[DataRequired(), NumberRange(min=1, max=100)])
    store = StringField('Store', validators=[DataRequired()])
    add = SubmitField('Add Employee/Manager')


class LocationForm(FlaskForm):
    city = StringField('City', validators=[DataRequired(), NumberRange(min=2)])
    state = StringField('State', validators=[DataRequired()])
    zip_code = DecimalField('Zip Code', validators=[DataRequired(), NumberRange(min=5, max=10)])
    add = SubmitField('Add Location')


class IngredientsForm(FlaskForm):
    order_date = StringField('Order Date', validators=[DataRequired(), Length(min=1, max=10)])
    ingredient_name = StringField('Ingredient Name', validators=[DataRequired(), Length(min=1, max=50)])
    ingredient_cost = IntegerField('Ingredient Cost', validators=[DataRequired()])
    order_id = IntegerField('Order ID', validators=[DataRequired(), NumberRange(min=1, max=1000)])
    submit = SubmitField('Add')


class SuppliersForm(FlaskForm):
    supplier_name = StringField('Supplier Name', validators=[DataRequired(), Length(min=1, max=50)])
    submit = SubmitField('Add')


class OrderForm(FlaskForm):
    date_time = StringField('Date', validators=[DataRequired(), NumberRange(min=1, max=10)])
    sale_amount = IntegerField('Sale Amount', validators=[DataRequired()])
    customer_id = IntegerField('Customer ID', validators=[DataRequired()])
    submit = SubmitField('Add')


class Customers(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=50)])
    last_name = IntegerField('Last Name', validators=[DataRequired(), Length(min=1, max=50)])
    email = StringField('Email', validators=[DataRequired()])
    phone_number = IntegerField('Phone Number', validators=[DataRequired(), NumberRange(min=1, max=20)])
    submit = SubmitField('Add')
