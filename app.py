import os
from flask import Flask, render_template, request
from forms import EmployeeManagerForm, LocationForm, IngredientsForm, SuppliersForm, OrderForm, Customers

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
ingredient_headers = ("ingredients_id", "order_date", "ingredient_name", "ingredient_cost", "order_id", "", "")
ingredient_values = (
    (1, "2021-01-01", "ground beef", 10, 101),
    (2, "2021-01-02", "buns", 5, 102),
    (3, "2021-01-03", "tomatoes", 5, 103),
    (4, "2021-01-04", "onions", 2, 104),
    (5, "2021-01-05", "ground beef", 10, 105),
    (6, "2021-01-06", "ketchup", 2, 106),
)

supplier_headers = ("supplier_id", "supplier_name", "", "")
supplier_values = (
    (100, "Johnson Ville"),
    (101, "Meat Industry")
)

order_headers = ("order_id", "date_time", "sale_amount", "", "")
order_values = (
    (300, "2021-01-01", 900),
    (301, "2021-01-02", 500),
    (302, "2021-01-03", 340)
)

customer_headers = ("customer_id", "first_name", "last_name", "email", "phone_number", "", "")
customer_values = (
    (5000, "Daniel", "Yu", "danielyu@osu.com", "808-254-1999"),
    (5001, "Alex", "Shin", "alexshin@osu.com", "702-153-0211")
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
    ingredient_form = IngredientsForm()
    supplier_form = SuppliersForm()

    return render_template("ingredients_suppliers.html", title='Register', ingredient_form=ingredient_form,
                           column_headers=ingredient_headers, sample_values=ingredient_values,
                           supplier_headers=supplier_headers, supplier_values=supplier_values,
                           supplier_form=supplier_form
                           )


@app.route("/orders-customers", methods=["GET", "POST"])
def orders_customers():
    order_form = OrderForm()
    customer_form = Customers()

    return render_template("orders_customers.html", title='Register', order_form=order_form,
                           customer_form=customer_form, order_headers=order_headers, order_values=order_values,
                           customer_headers=customer_headers, customer_values=customer_values
                           )




if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3001))
    app.run(port=port, debug=True)
