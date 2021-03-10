from flask import Flask, render_template, request, url_for, redirect
from forms import EmployeeManagerForm, LocationForm, IngredientsForm, SuppliersForm, OrderForm, Customers, \
    SubmitCustomers
from db_connector import connect_to_database, execute_query

app = Flask(__name__)

# required to keep sessions secure
# need to create a config file to keep key and DB configs later
app.config['SECRET_KEY'] = '7cd4739b6ecbf78e2fb020b7f663a979'

# headers for tables displaying data
headers = ['First Name', 'Last Name', 'Start Date', 'Vacation', 'Managed by', 'Location', "", ""]
location_headers = ['City', 'State', 'Zip Code', '', '']


# route for the homepage (root) is defined, but it's html is just the base
@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


# validator helper function to specify which form was submitted
def validator(data_list):
    all_valid = True

    for value in data_list:
        if value is None:
            all_valid = False

    return all_valid


# route for the orders & customers page
@app.route("/orders-customers", methods=["GET", "POST"])
def orders_customers():
    # create a reference to the form (objects)
    order_form = OrderForm(request.form)
    customer_form = Customers(request.form)
    search_form = SubmitCustomers(request.form)

    # establish a connection to the db
    db_connection = connect_to_database()

    # column headers for each table
    orders_customers_h = ["Date", "Customer ID", "Sales Amount ($)", "First Name", "Last Name", "E-mail",
                          "Phone Number", "", ""]
    customer_headers = ["First Name", "Last Name", "E-mail", "Phone Number", "Location", "", ""]

    # get the user's input values from the search box (if any)
    search_data = search_form.submit_id.data

    # check if there is a POST request, that is not from the search box
    if request.method == 'POST' and search_data == "":
        # get the data from each field of the Order form
        date_time = order_form.date_time.data
        sale_amount = order_form.sale_amount.data
        customer_id = order_form.customer_id.data

        # get the data from each field of the Customer form
        first_name = customer_form.first_name.data
        last_name = customer_form.last_name.data
        email = customer_form.email.data
        phone_number = customer_form.phone_number.data
        location = customer_form.location.data

        # place the data in tuples for it to be iterable and not mutable
        order_input_data = (date_time, sale_amount, customer_id,)
        customer_input_data = (first_name, last_name, email, phone_number,)

        # query for adding a new Order into the db
        order_input_query = \
            "INSERT INTO Orders (date_time, sale_amount, customer_num) " \
            "VALUES (%s, %s, %s);"

        # query for adding a new Customer into the db
        customer_input_query = \
            "INSERT INTO Customers (first_name, last_name, email, phone_number) " \
            "VALUES (%s, %s, %s, %s);"

        # adding a new Customer also involves adding them to the Customers_Locations intersection table
        # here, we get the location_id based on the location that the user selected
        get_location_id_query = "SELECT store_id FROM `Locations` WHERE city = (%s)"
        get_location_id_results = execute_query(db_connection, get_location_id_query, (location,)).fetchall()

        # once our webpage has two forms present, we need to check which one the user is submitting
        # since the user can only submit one form at any time, the boolean value returned from validator()
        # allows us to know which form has data.

        if validator(order_input_data):
            # execute the query and commit it to the db for changes to be permanent
            execute_query(db_connection, order_input_query, order_input_data)

        elif validator(customer_input_data):
            execute_query(db_connection, customer_input_query, customer_input_data)

            # get latest customer_id that was added (just now)
            get_customer_id_query = "SELECT customer_id FROM `Customers` ORDER BY customer_id DESC LIMIT 1"
            get_customer_id_results = execute_query(db_connection, get_customer_id_query).fetchall()

            # add the customer_id and location_id into the intersection table
            add_customer_locations = "INSERT INTO Customers_Locations (customer_fk_id, store_fk_id) VALUES (%s, %s);"
            customer_locations = (get_customer_id_results[0][0], get_location_id_results[0][0],)

            execute_query(db_connection, add_customer_locations, customer_locations)
        # refresh the page once the form is submitted
        return redirect(url_for('orders_customers'))

    else:
        # queries for displaying the Orders and Customers 'overview' tables
        orders_query = \
            "SELECT date_time, customer_id, sale_amount, first_name, last_name, email, phone_number, order_id " \
            "FROM `Customers` " \
            "INNER JOIN Orders ON Orders.customer_num = Customers.customer_id ORDER BY date_time;"

        customers_query = \
            "SELECT first_name, last_name, email, phone_number, city AS location, customer_id FROM `Customers` " \
            "INNER JOIN Customers_Locations ON Customers_Locations.customer_fk_id = Customers.customer_id " \
            "INNER JOIN Locations ON Locations.store_id = Customers_Locations.store_fk_id ORDER BY last_name;"

        # execute the query to retrieve the table data from the db
        order_results = execute_query(db_connection, orders_query).fetchall()
        customer_results = execute_query(db_connection, customers_query).fetchall()

        customer_id_choices = []
        location_choices = []

        for choices in customer_results:
            customer_id_choices.append(choices[5])
            if choices[4] not in location_choices:
                location_choices.append(choices[4])

        # set the 'choices' option for customer_id for the OrderForm form
        order_form.customer_id.choices = customer_id_choices
        customer_form.location.choices = location_choices

        if request.method == 'POST' and search_data != "":
            search_query = \
                "SELECT date_time, customer_id, sale_amount, first_name, last_name, email, phone_number " \
                "FROM `Customers` " \
                "INNER JOIN Orders ON Orders.customer_num = Customers.customer_id " \
                "WHERE first_name LIKE (%s);"

            search_query = execute_query(db_connection, search_query, ("%" + search_data + "%",)).fetchall()

            if search_query:
                order_results = search_query

        # render the webpage with all the data retrieved from the db
        return render_template("orders_customers.html", title='Add/Edit/Delete Orders & Customers',
                               order_form=order_form, customer_form=customer_form,
                               customer_headers=customer_headers, customer_values=customer_results,
                               orders_customers_h=orders_customers_h, orders_customers_v=order_results,
                               search_form=search_form, city_name=location_choices)


# route for the ingredients & suppliers page
@app.route("/ingredients-suppliers", methods=["GET", "POST"])
def ingredients_suppliers():
    db_connection = connect_to_database()
    ingredient_form = IngredientsForm()
    supplier_form = SuppliersForm()

    ingredient_suppliers_h = ["Order Date", "Name", "Cost ($)", "Order ID", "", ""]
    suppliers_headers = ["Name", "", ""]

    # for POST requests
    if request.method == 'POST':
        order_date = ingredient_form.order_date.data
        ingredient_name = ingredient_form.ingredient_name.data
        ingredient_cost = ingredient_form.ingredient_cost.data
        supplier = ingredient_form.supplier.data
        order_id = ingredient_form.order_id.data

        ingredient_input_query = "INSERT INTO Ingredients (order_date, ingredient_name, ingredient_cost, order_num) " \
                                 "VALUES (%s, %s, %s, %s);"

        supplier_input_query = "INSERT INTO Suppliers (supplier_name) VALUES (%s);"
        get_supplier_id_query = "SELECT supplier_id FROM `Suppliers` WHERE supplier_name = (%s)"
        get_supplier_id_results = execute_query(db_connection, get_supplier_id_query, (supplier,)).fetchall()

        # grab user's input from add new Ingredient form, and INSERT into the db
        ingredients_input_data = (order_date, ingredient_name, ingredient_cost, order_id)
        supplier_name = supplier_form.supplier_name.data
        supplier_input_data = (supplier_name,)

        if validator(ingredients_input_data) is True:
            execute_query(db_connection, ingredient_input_query, ingredients_input_data)

            # get latest ingredient ID, that was just created
            get_ingredient_id_query = "SELECT ingredient_id FROM `Ingredients` ORDER BY ingredient_id DESC LIMIT 1"
            get_ingredient_id_results = execute_query(db_connection, get_ingredient_id_query).fetchall()

            # add ingredient_id and supplier_id to the Ingredients_Suppliers intersection table, to establish a M:M
            # relationship
            add_ingredient_supplier_IDs = "INSERT INTO Ingredients_Suppliers (ing_id, sup_id) VALUES (%s, %s)"
            IDs_parsed = (get_ingredient_id_results[0][0], get_supplier_id_results[0][0])
            execute_query(db_connection, add_ingredient_supplier_IDs, IDs_parsed)

        elif validator(supplier_input_data) is True:
            execute_query(db_connection, supplier_input_query, supplier_input_data)

        return redirect(url_for('ingredients_suppliers'))

    elif request.method == 'GET':
        # for GET requests
        ingredients_query = "SELECT order_date, ingredient_name, ingredient_cost, order_num, ingredient_id FROM " \
                            "`Ingredients`; "
        suppliers_query = "SELECT supplier_name, supplier_id FROM Suppliers;"
        order_id_query = "SELECT order_id FROM `Orders`;"

        supplier_choices = []
        order_id_choices = []
        ingredients_supplied_choices = []

        # execute the above select queries and retrieve the data
        ingredient_results = execute_query(db_connection, ingredients_query).fetchall()
        suppliers_results = execute_query(db_connection, suppliers_query).fetchall()
        order_id_results = execute_query(db_connection, order_id_query).fetchall()

        # the data retrieved from the db are a tuple of tuples, here we take each individual tuple and add to a list (to
        # get a list of all items)
        for choices in ingredient_results:
            order_id_choices.append(choices[3])

        for choices in suppliers_results:
            supplier_choices.append(choices[0])

        for choices in ingredient_results:
            ingredients_supplied_choices.append(choices[1])

        # from the list of items, assign them to each Form's choices option
        ingredient_form.supplier.choices = supplier_choices
        ingredient_form.order_id.choices = order_id_choices
        supplier_form.ingredients_supplied.choices = ingredients_supplied_choices

        return render_template("ingredients_suppliers.html", title='Add/Edit/Delete Ingredients & Suppliers',
                               ingredient_form=ingredient_form,
                               suppliers_headers=suppliers_headers, suppliers_values=suppliers_results,
                               supplier_form=supplier_form, ingredient_suppliers_h=ingredient_suppliers_h,
                               ingredient_suppliers_v=ingredient_results, order_nums=order_id_results)


# route for employees & locations page
@app.route("/employees-locations", methods=['GET', 'POST'])
def employees_locations():
    db_connection = connect_to_database()
    employee_manager_form = EmployeeManagerForm(request.form)
    location_form = LocationForm(request.form)

    # for POST requests
    if request.method == 'POST':
        first_name = employee_manager_form.first_name.data
        last_name = employee_manager_form.last_name.data
        start_date = employee_manager_form.start_date.data

        if employee_manager_form.status.data is True:
            status = "vacation"
        else:
            status = "active"

        manager = employee_manager_form.manager.data

        if manager is True:
            managed_by = None
        else:
            managed_by_query = "SELECT manager_id FROM Managers WHERE first_name = %s;"
            managed_by_result = execute_query(db_connection, managed_by_query,
                                              str(employee_manager_form.managed_by.data)).fetchall()
            managed_by = managed_by_result

        store_query = "SELECT store_id FROM Locations WHERE city = %s;"
        store_result = execute_query(db_connection, store_query, str(employee_manager_form.store.data)).fetchall()
        store = store_result

        city = location_form.city.data
        state = location_form.state.data
        zip_code = location_form.zip_code.data

        # employees_managers
        if managed_by is not None:
            employee_input_data = (first_name, last_name, start_date, status, managed_by, store)
            employee_input_query = "INSERT INTO Employees (first_name, last_name, start_date, status, emp_manager_id, emp_store_id) \
                                VALUES (%s, %s, %s, %s, %s, %s);"
        else:
            employee_input_data = (first_name, last_name, start_date, status, store)
            employee_input_query = "INSERT INTO Employees (first_name, last_name, start_date, status, emp_store_id) \
                                VALUES (%s, %s, %s, %s, %s);"

        manager_input_data = None
        if manager is True:
            manager_input_data = (first_name, last_name, status, store)
            manager_input_query = "INSERT INTO Managers (first_name, last_name, status, manager_store_id) \
                                   VALUES (%s, %s, %s, %s);"

        # locations
        location_input_data = (city, state, zip_code)
        location_input_query = "INSERT INTO Locations (`city`, state, zip_code) \
                                VALUES (%s, %s, %s);"

        if validator(location_input_data):
            execute_query(db_connection, location_input_query, location_input_data)
            db_connection.commit()

        if validator(employee_input_data):
            execute_query(db_connection, employee_input_query, employee_input_data)
            if manager_input_data is not None:
                execute_query(db_connection, manager_input_query, manager_input_data)

            db_connection.commit()

            # add manager_num to Employees table
            db_connection = connect_to_database()
            if manager_input_data is not None:
                last_added_employee_query = "SELECT employee_id FROM Employees ORDER BY employee_id DESC LIMIT 1;"
                last_added_employee_result = execute_query(db_connection, last_added_employee_query).fetchone()

                last_added_manager_query = "SELECT manager_id FROM Managers ORDER BY manager_id DESC LIMIT 1;"
                last_added_manager_result = execute_query(db_connection, last_added_manager_query).fetchone()

                add_manager_num_query = "UPDATE Employees SET manager_num=%s WHERE employee_id=%s;"
                add_manager_num_data = (last_added_manager_result, last_added_employee_result)
                execute_query(db_connection, add_manager_num_query, add_manager_num_data)

        return redirect(url_for("employees_locations"))

    # for GET requests
    # employees
    employees_managers_query = "SELECT \
                                    Employees.first_name, Employees.last_name, \
                                    Employees.start_date, Employees.status, \
                                    CONCAT(Managers.first_name, ' ', Managers.last_name) AS ManagedBy, \
	                                Locations.city, Employees.employee_id \
                                FROM Employees \
                                LEFT JOIN Managers ON Managers.manager_id = Employees.emp_manager_id \
                                LEFT JOIN Locations ON Locations.store_id = Employees.emp_store_id \
                                ORDER BY start_date;"
    employees_managers_results = execute_query(db_connection, employees_managers_query).fetchall()
    # print(employees_managers_results[0])

    # locations
    location_query = "SELECT city, state, zip_code, store_id FROM Locations;"
    location_results = execute_query(db_connection, location_query).fetchall()

    # dropdowns
    managed_by_name_query = "SELECT first_name FROM Managers;"
    managed_by_name_results = execute_query(db_connection, managed_by_name_query).fetchall()
    managed_by_choices = []

    manager_id_name = "SELECT manager_id, CONCAT(first_name, ' ', last_name) AS full_name FROM Managers;"
    manager_id_name_results = execute_query(db_connection, manager_id_name).fetchall()

    for choices in managed_by_name_results:
        managed_by_choices.append(choices[0])

    employee_manager_form.managed_by.choices += managed_by_choices

    store_city_query = "SELECT city FROM Locations;"
    store_city_results = execute_query(db_connection, store_city_query).fetchall()
    store_city_choices = []

    for choices in store_city_results:
        store_city_choices.append(choices[0])

    employee_manager_form.store.choices = store_city_choices

    return render_template('employees_locations.html', headers=headers, data=employees_managers_results,
                           location_headers=location_headers,
                           location_data=location_results, emp_man_form=employee_manager_form, loc_form=location_form,
                           city_name=store_city_results,
                           managers=manager_id_name_results
                           )


@app.route("/delete_order/<int:id>", methods=['GET', 'POST'])
def delete_order(id):
    """deletes an order with the given order id"""
    db_connection = connect_to_database()
    delete_order_query = "DELETE FROM Orders WHERE order_id = %s;"
    data = (id,)
    execute_query(db_connection, delete_order_query, data)
    return redirect(url_for("orders_customers"))


@app.route("/delete_customer/<int:id>", methods=['GET', 'POST'])
def delete_customer(id):
    """deletes a customer with the given customer id"""
    db_connection = connect_to_database()
    delete_customer_query = "DELETE FROM Customers WHERE customer_id = %s;"
    delete_customer_data = (id,)
    execute_query(db_connection, delete_customer_query, delete_customer_data)

    # also delete from customers_locations M:M table
    delete_customers_locations_query = "DELETE FROM Customers_Locations WHERE customer_fk_id=%s;"
    delete_customers_locations_data = (id,)
    execute_query(db_connection, delete_customers_locations_query, delete_customers_locations_data)
    return redirect(url_for("orders_customers"))


@app.route('/delete_ingredient/<int:id>')
def delete_ingredient(id):
    """deletes a ingredient with the given id"""
    db_connection = connect_to_database()
    print("We're at delete query!")
    delete_intersection_query = "DELETE FROM Ingredients_Suppliers WHERE ing_id = %s"
    delete_ingredient_query = "DELETE FROM Ingredients WHERE ingredient_id = %s"
    data = (id,)
    execute_query(db_connection, delete_intersection_query, data)
    execute_query(db_connection, delete_ingredient_query, data)

    return redirect(url_for("ingredients_suppliers"))


@app.route('/delete_supplier/<int:id>', methods=['GET', 'POST'])
def delete_supplier(id):
    """deletes a supplier with the given id"""
    db_connection = connect_to_database()
    print("We're at delete query for deleting a supplier!")
    delete_intersection_query = "DELETE FROM Ingredients_Suppliers WHERE sup_id = %s"
    delete_supplier_query = "DELETE FROM Suppliers WHERE supplier_id = %s"
    data = (id,)
    execute_query(db_connection, delete_intersection_query, data)
    execute_query(db_connection, delete_supplier_query, data)

    return redirect(url_for("ingredients_suppliers"))


@app.route('/delete_location/<int:id>', methods=['GET', 'POST'])
def delete_location(id):
    """deletes a store location with the given id"""
    db_connection = connect_to_database()
    delete_intersection_query = "DELETE FROM Customers_Locations WHERE store_fk_id = %s"
    delete_location_query = "DELETE FROM Locations WHERE store_id = %s;"
    data = (id,)
    execute_query(db_connection, delete_intersection_query, data)
    execute_query(db_connection, delete_location_query, data)
    return redirect(url_for("employees_locations"))


@app.route('/delete_employee/<int:id>')
def delete_employee(id):
    db_connection = connect_to_database()
    delete_employee_query = "DELETE FROM Employees WHERE employee_id = %s"
    data = (id,)
    results = execute_query(db_connection, delete_employee_query, data)

    # delete managers if not in employee table after deleting employee who might be a manager
    delete_manager_query = "DELETE FROM Managers WHERE NOT EXISTS (SELECT 1 FROM Employees WHERE Employees.manager_num = Managers.manager_id);"
    execute_query(db_connection, delete_manager_query)

    return redirect(url_for("employees_locations"))


@app.route('/update_order/<int:id>', methods=['POST', 'GET'])
def update_order(id):
    """update an order with the given id"""
    db_connection = connect_to_database()

    if request.method == 'POST':
        order_date = request.form['date']
        customer_id = request.form['customer_id']

        sales_amount = request.form['sales_amount']

        update_order_query = \
            "UPDATE Orders SET date_time=%s, sale_amount=%s, customer_num=%s WHERE order_id=%s;"

        update_order_data = (order_date, sales_amount, customer_id, id)
        execute_query(db_connection, update_order_query, update_order_data)

        # update order_date in ingredients table as well
        update_date_query = "UPDATE Ingredients SET order_date=%s WHERE order_num=%s;"
        update_date_data = (order_date, id)
        execute_query(db_connection, update_date_query, update_date_data)

    return redirect(url_for("orders_customers"))


@app.route('/update_customer/<int:id>', methods=['POST', 'GET'])
def update_customer(id):
    """update a customer with the given id"""
    db_connection = connect_to_database()

    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        location = request.form['location']

        update_customer_query = \
            "UPDATE Customers SET first_name=%s, last_name=%s, email=%s, phone_number=%s WHERE customer_id=%s;"

        update_customer_data = \
            (first_name, last_name, email, phone_number, id)

        execute_query(db_connection, update_customer_query, update_customer_data)

        # also update the customer_locations M:M table row with changed location
        new_location_query = "SELECT store_id FROM Locations WHERE city=%s;"
        new_location_data = (location)
        new_location_id = execute_query(db_connection, new_location_query, new_location_data).fetchone()

        update_customers_locations_query = \
            "UPDATE Customers_Locations SET store_fk_id=%s WHERE customer_fk_id=%s;"

        update_customers_locations_data = (new_location_id, id)
        execute_query(db_connection, update_customers_locations_query, update_customers_locations_data)

    return redirect(url_for("orders_customers"))


@app.route('/update_ingredient/<int:id>', methods=['POST', 'GET'])
def update_ingredient(id):
    """update a ingredient with the given id"""
    db_connection = connect_to_database()

    if request.method == "POST":
        order_date = request.form['order_date']
        ingredient_name = request.form['ingredient_name']
        ingredient_cost = request.form['ingredient_cost']
        order_num = request.form['order_num']

        update_query = \
            "UPDATE Ingredients SET order_date = %s, ingredient_name = %s, ingredient_cost = %s, order_num = %s " \
            "WHERE ingredient_id =  %s;"

        data = (order_date, ingredient_name, ingredient_cost, order_num, id)
        execute_query(db_connection, update_query, data)

    return redirect(url_for("ingredients_suppliers"))


@app.route('/update_supplier/<int:id>', methods=['POST', 'GET'])
def update_supplier(id):
    """update a supplier with the given id"""
    db_connection = connect_to_database()

    if request.method == "POST":
        supplier_name = request.form['supplier_name']

        update_query = \
            "UPDATE Suppliers SET supplier_name = %s" \
            "WHERE supplier_id =  %s;"

        data = (supplier_name, id)
        execute_query(db_connection, update_query, data)

    return redirect(url_for("ingredients_suppliers"))


@app.route('/update_employee/<int:id>', methods=['POST', 'GET'])
def update_employee(id):
    """update an employee with the given employee id"""
    db_connection = connect_to_database()

    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        start_date = request.form['start_date']
        vacation = request.form['vacation']

        # find the manager_id of the new manager entered in the update form for employee
        managed_by = request.form['managed_by']
        new_manager = managed_by.split(" ", 1)
        new_manager_query = "SELECT manager_id FROM Managers WHERE Managers.first_name = %s AND Managers.last_name = %s"
        new_manager_data = (new_manager[0], new_manager[1])

        print("new_manager_data = ", new_manager_data)
        # new_manager_data = (new_manager[0], str(new_manager[1:]))

        new_manager_id = execute_query(db_connection, new_manager_query, new_manager_data).fetchone()

        # find the store_id of the new location entered in the update form for employee
        location = request.form['location']
        new_location_query = "SELECT store_id FROM Locations WHERE Locations.city = %s"
        new_location_id = execute_query(db_connection, new_location_query, location).fetchone()

        update_query = \
            "UPDATE Employees SET first_name = %s, last_name=%s, start_date=%s, status=%s, emp_manager_id=%s, emp_store_id=%s WHERE employee_id = %s;"

        data = (first_name, last_name, start_date, vacation, new_manager_id, new_location_id, id)
        result = execute_query(db_connection, update_query, data)

        # if also a manager
        manager_num_query = "SELECT manager_num FROM Employees WHERE Employees.employee_id = %s"
        manager_num_data = (id,)
        manager_num_result = execute_query(db_connection, manager_num_query, manager_num_data).fetchone()
        if manager_num_result is not None:
            manager_update_query = "UPDATE Managers SET first_name=%s, last_name=%s, status=%s, manager_store_id=%s WHERE manager_id = %s;"
            manager_update_data = (first_name, last_name, vacation, new_location_id, manager_num_result)
            execute_query(db_connection, manager_update_query, manager_update_data)

    return redirect(url_for("employees_locations"))


@app.route('/update_location/<int:id>', methods=['POST', 'GET'])
def update_location(id):
    """update a store location with the given store id"""
    db_connection = connect_to_database()

    if request.method == "POST":
        location_city = request.form['location_city']
        location_state = request.form['location_state']
        location_zip_code = request.form['location_zip_code']

        update_query = \
            "UPDATE Locations SET city = %s, state = %s, zip_code = %s WHERE store_id = %s;"

        data = (location_city, location_state, location_zip_code, id)
        result = execute_query(db_connection, update_query, data)

    return redirect(url_for("employees_locations"))
