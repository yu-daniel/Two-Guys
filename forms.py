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
    ingredient_id = IntegerField('Ingredient ID', validators=[DataRequired(), NumberRange(min=1, max=1000)])
    order_date = IntegerField('Order Date', validators=[DataRequired(), NumberRange(min=1, max=10)])
    ingredient_name = StringField('Ingredient Name', validators=[DataRequired(), Length(min=1, max=50)])
    ingredient_cost = IntegerField('Ingredient ID', validators=[DataRequired()])
    order_id = IntegerField('Order ID', validators=[DataRequired(), NumberRange(min=1, max=1000)])
    submit = SubmitField('Add Ingredient')

class SuppliersForm(FlaskForm):
    supplier_id = IntegerField('Supplier ID', validators=[DataRequired(), NumberRange(min=1, max=1000)])
    supplier_name = StringField('Supplier Name', validators=[DataRequired(), Length(min=1, max=50)])
    submit = SubmitField('Add Supplier')

class OrderForm(FlaskForm):
    order_id = IntegerField('Ingredient ID', validators=[DataRequired(), NumberRange(min=1, max=1000)])
    date_time = StringField('Date', validators=[DataRequired(), NumberRange(min=1, max=10)])
    sale_amount = IntegerField('Sale Amount', validators=[DataRequired()])
    submit = SubmitField('Add Order')

class CustomersForm(FlaskForm):
    customer_id = IntegerField('Customer ID', validators=[DataRequired(), NumberRange(min=1, max=1000)])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=50)])
    last_name = IntegerField('Last Name', validators=[DataRequired(), Length(min=1, max=50)])
    email = StringField('Email', validators=[DataRequired()])
    phone_number = IntegerField('Order ID', validators=[DataRequired(), NumberRange(min=1, max=20)])
    submit = SubmitField('Add Customer')
