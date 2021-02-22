from flask_wtf import FlaskForm
from wtforms import StringField, DateField, BooleanField, DecimalField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange

class OrdersSearchForm(FlaskForm):
    search_customer = StringField('Search Customer:')
    search_button = SubmitField('Go!')

class EmployeeManagerForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), NumberRange(min=1, max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), NumberRange(min=1, max=50)])
    start_date = DateField('Start Date', validators=[DataRequired()], render_kw={"placeholder": "Year/Month/Date..."})
    status = BooleanField('Vacation')
    manager = BooleanField('Manager')
    managed_by = SelectField('Managed by', choices=['None'])
    store = SelectField('Store')
    add = SubmitField('Add')


class LocationForm(FlaskForm):
    city = StringField('City', validators=[DataRequired(), NumberRange(min=2)])
    state = StringField('State', validators=[DataRequired()])
    zip_code = DecimalField('Zip Code', validators=[DataRequired(), NumberRange(min=5, max=10)])
    add = SubmitField('Add')


class IngredientsForm(FlaskForm):
    order_date = StringField('Order Date', validators=[DataRequired(), Length(min=1, max=10)], render_kw={"placeholder": "Year/Month/Date..."})
    ingredient_name = StringField('Ingredient Name', validators=[DataRequired(), Length(min=1, max=50)])
    ingredient_cost = IntegerField('Ingredient Cost', validators=[DataRequired()])
    order_id = SelectField('Order ID')
    supplier = SelectField('Supplier')
    submit = SubmitField('Add')


class SuppliersForm(FlaskForm):
    supplier_name = StringField('Supplier Name', validators=[DataRequired(), Length(min=1, max=50)])
    ingredients_supplied = SelectField('Ingredients Supplied')
    submit = SubmitField('Add')


class OrderForm(FlaskForm):
    date_time = StringField('Date', validators=[DataRequired(), NumberRange(min=1, max=10)], render_kw={"placeholder": "Year/Month/Date..."})
    sale_amount = IntegerField('Sale Amount', validators=[DataRequired()])
    customer_id = SelectField('Customer ID')
    submit = SubmitField('Add')


class Customers(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=50)])
    email = StringField('Email', validators=[DataRequired()])
    phone_number = IntegerField('Phone Number', validators=[DataRequired(), NumberRange(min=1, max=20)])
    location = SelectField('Location')
    submit = SubmitField('Add')

# Reference
# Description: use of render_kw attribute for adding placeholder text in the Field
# Link: https://stackoverflow.com/questions/9749742/wtforms-can-i-add-a-placeholder-attribute-when-i-init-a-field
# render_kw={"placeholder": "Enter Customer ID..."}


class SubmitCustomers(FlaskForm):
    submit_id = StringField(label='', render_kw={"placeholder": "Enter Customer First Name..."})
    submit = SubmitField('Search')
