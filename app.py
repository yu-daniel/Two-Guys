import os
from flask import Flask, render_template, request
from forms import EmployeeManagerForm, LocationForm, IngredientsForm

app = Flask(__name__)

# required to keep sessions secure
# need to create a config file to keep key and DB configs later
app.config['SECRET_KEY'] = '7cd4739b6ecbf78e2fb020b7f663a979'

# dummy data
headers = ['Name', 'Start Date', 'Vacation', 'Manager', 'Managed by', 'Location']
data = [
	['Alex Shin', '10/25/2011', 'Yes', 'No', 'Daniel Yu', 'LA'], 
	['Daniel Yu', '11/11/2004', 'No', 'Yes', 'None', 'LA']
]

# Just some dummy data for Step 3

column_headers = ("ingredients_id", "order_date", "ingredient_name", "ingredient_cost", "order_id")
sample_values = (
    (1, "2021-01-01", "ground beef", 10, 101),
    (2, "2021-01-02", "buns", 5, 102),
    (3, "2021-01-03", "tomatoes", 5, 103),
    (4, "2021-01-04", "onions", 2, 104),
    (5, "2021-01-05", "ground beef", 10, 105),
    (6, "2021-01-06", "ketchip", 2, 106),
)

# route for the homepage (root) is defined, but it's html is just the base
@app.route("/", methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route("/people", methods=['GET', 'POST'])
def people():
	emp_man_form = EmployeeManagerForm()
	loc_form = LocationForm()
	return render_template('emp_loc.html', headers=headers, data=data, emp_man_form=emp_man_form, loc_form=loc_form)

# route for the ingredients & suppliers page
@app.route("/ingredients-suppliers", methods=["GET", "POST"])
def ingredients_suppliers():
    form = IngredientsForm()
    return render_template("ingredients_suppliers.html", title='Register', form=form,
                           column_headers=column_headers, sample_values=sample_values)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 3001))
	app.run(port=port)