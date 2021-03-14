from flask_wtf import FlaskForm
from wtforms import StringField, DateField, BooleanField, DecimalField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange, Email


class EmployeeManagerForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=50)])
    start_date = DateField('Start Date', validators=[DataRequired()], render_kw={"placeholder": "YYYY-MM-DD"})
    status = BooleanField('Vacation')
    manager = BooleanField('Manager')
    managed_by = SelectField('Managed by', validators=[DataRequired()], choices=['None'])
    store = SelectField('Store', validators=[DataRequired()])
    add = SubmitField('Add')


class LocationForm(FlaskForm):
    city = StringField('City', validators=[DataRequired(), Length(min=2)])
    state = StringField('State', validators=[DataRequired(), Length(min=2)])
    zip_code = DecimalField('Zip Code', validators=[DataRequired(), NumberRange(min=5, max=10)])
    add = SubmitField('Add')


class IngredientsForm(FlaskForm):
    order_date = StringField('Order Date', validators=[DataRequired()], render_kw={"placeholder": "YYYY-MM-DD"})
    ingredient_name = StringField('Ingredient Name', validators=[DataRequired(), Length(min=1, max=50)])
    ingredient_cost = IntegerField('Ingredient Cost', validators=[DataRequired(), NumberRange(min=1)])
    order_id = SelectField('Order ID', validators=[DataRequired()])
    supplier = SelectField('Supplier', validators=[DataRequired()])
    submit = SubmitField('Add')


class SuppliersForm(FlaskForm):
    supplier_name = StringField('Supplier Name', validators=[DataRequired(), Length(min=1, max=50)])
    ingredients_supplied = SelectField('Ingredients Supplied')
    submit = SubmitField('Add')


class OrderForm(FlaskForm):
    date_time = StringField('Date', validators=[DataRequired()], render_kw={"placeholder": "YYYY-MM-DD"})
    sale_amount = IntegerField('Sale Amount', validators=[DataRequired(), NumberRange(min=1)])
    customer_id = SelectField('Customer ID', validators=[DataRequired()])
    submit = SubmitField('Add')


class Customers(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = IntegerField('Phone Number', validators=[DataRequired(), NumberRange(min=1, max=20)])
    location = SelectField('Location', validators=[DataRequired()])
    submit = SubmitField('Add')

class SubmitCustomers(FlaskForm):
    submit_id = StringField(label='', render_kw={"placeholder": "Customer First Name"})
    submit = SubmitField('Search')
