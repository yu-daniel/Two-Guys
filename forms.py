from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length

class IngredientsForm(FlaskForm):
	ingredient_id = IntegerField('Ingredient ID', validators = [DataRequired(), NumberRange(min=1, max=1000)])
	order_date = IntegerField('Order Date', validators = [DataRequired(), NumberRange(min=1, max=10)])
	ingredient_name = StringField('Ingredient Name', validators = [DataRequired(), Length(min=1, max=50)])
	ingredient_cost = IntegerField('Ingredient ID', validators = [DataRequired()])
	order_id = IntegerField('Order ID', validators = [DataRequired(), NumberRange(min=1, max=1000)])
	submit = SubmitField('Submit')