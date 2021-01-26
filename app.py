import os
from flask import Flask, render_template
from forms import EmployeeManagerForm, LocationForm

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

@app.route("/", methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route("/people", methods=['GET', 'POST'])
def people():
	emp_man_form = EmployeeManagerForm()
	loc_form = LocationForm()
	return render_template('emp_loc.html', headers=headers, data=data, emp_man_form=emp_man_form, loc_form=loc_form)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5001))
	app.run(port=port)