-- for the ingredient-suppliers web page:
-- #############################################################################################################################################################################################

-- get all supplier IDs and supplier names for the Suppliers dropdown menu for the form.
SELECT supplier_id, supplier_name FROM `Suppliers`;

-- get all ingredient IDs and ingredient names for the Ingredients dropdown menu for the form.
SELECT ingredient_id, ingredient_name FROM `Ingredients`;

-- get all the field names (i.e. attribute names) and the corresponding values for the Ingredients table.
SELECT order_date, ingredient_name, ingredient_cost, order_num FROM `Ingredients`;

-- get all the field names (i.e. attribute names) and the corresponding values for the Suppliers table.
SELECT supplier_name FROM `Suppliers`;

--
SELECT ingredient_id FROM `Ingredients` ORDER BY ingredient_id DESC LIMIT 1

-- get all the field names (i.e. attribute names) and the corresponding values for the Ingredients_Suppliers intersection table.
SELECT ingredient_name, supplier_name FROM `Ingredients`
INNER JOIN Ingredients_Suppliers ON Ingredients_Suppliers.ing_id = Ingredients.ingredient_id
INNER JOIN Suppliers ON Suppliers.supplier_id = Ingredients_Suppliers.sup_id
ORDER BY ingredient_name;

-- add a new Ingredient
INSERT IGNORE INTO Ingredients (order_date, ingredient_name, ingredient_cost, order_num) VALUES (:order_dateInput, :ingredient_nameInput, :ingredient_costInput, :order_numInput);

-- add a new Supplier
INSERT IGNORE INTO Suppliers (supplier_name) VALUES (:supplier_nameInput);

-- relate an Ingredient with a Supplier for creating a M:M relationship
INSERT IGNORE INTO Ingredients_Suppliers (ing_id, sup_id) VALUES (:ing_idInput, :sup_idInput);

-- update an entry in the Ingredients table
UPDATE Ingredients SET order_date = :order_dateInput, ingredient_name = :ingredient_nameInput, ingredient_cost = :ingredient_costInput, order_num = :order_numInput WHERE ingredient_id =  :ingredient_id_from_editable_in_table;

-- update an entry in the Suppliers table
UPDATE Suppliers SET supplier_name = :supplier_nameInput WHERE supplier_id = :supplier_id__from_editable_in_table;

-- delete an enty in the Ingredients table
DELETE FROM Ingredients WHERE ingredient_id = :ingredient_id_from_ingredients_table

-- delete an entry in the Suppliers table
DELETE FROM Suppliers WHERE supplier_id = :supplier_id_from_suppliers_table

-- remove a M:M relationship between an Ingredient and a Supplier ## NOTE: so we might need like another form with input fields where the user can enter ing_id & sup_id
DELETE FROM Ingredients_Suppliers WHERE ing_id = :ingredient_idInput AND sup_id = :sup_idInput;


-- for the orders-customers web page:
-- #############################################################################################################################################################################################

-- get all the attribute (i.e. column names) and their values from the Customers and Orders table (by joining them together)
-- this should allow the generation of the Orders table
SELECT date_time, customer_id, sale_amount, first_name, last_name, email, phone_number FROM `Customers`
INNER JOIN Orders ON Orders.customer_num = Customers.customer_id
ORDER BY date_time;

-- get all the attribute (i.e. column names) and their values from the Customers, Locations, and Customers_Locations tables (by joining them together)
SELECT first_name, last_name, email, phone_number, city AS location FROM `Customers`
INNER JOIN Customers_Locations ON Customers_Locations.customer_fk_id = Customers.customer_id
INNER JOIN Locations ON Locations.store_id = Customers_Locations.store_fk_id
ORDER BY last_name;

-- get latest customer_id that was last added
SELECT customer_id FROM `Customers` ORDER BY customer_id DESC LIMIT 1

-- add a new Customer
INSERT IGNORE INTO Customers (first_name, last_name, email, phone_number) VALUES (:first_nameInput, :last_nameInput, :emailInput, :phone_numberInput);

-- add a new Order
INSERT IGNORE INTO Orders (date_time, sale_amount, customer_num) VALUES (:date_timeInput, :sale_amountInput, :customer_numInput);

-- add the customer_id and location_id into the intersection table
INSERT IGNORE INTO Customers_Locations (customer_fk_id, store_fk_id) VALUES (:customer_fk_idInput, store_fk_idInput);

-- update an entry in the Customers table
UPDATE Customers SET first_name = :first_nameInput, last_name = :last_nameInput, email = :emailInput, phone_number = :phone_numberInput WHERE customer_id =  :customer_id_from_editable_in_table;

-- update an entry in the Orders table
UPDATE Orders SET date_time = :date_timeInput, sale_amount = :sale_amountInput, customer_num = :customer_numInput WHERE order_id = :order_id__from_editable_in_table

-- delete an enty in the Customers table
DELETE FROM Customers WHERE customer_id = :customer_id_from_customers_table

-- delete an entry in the Orders table
DELETE FROM Orders WHERE order_id = :order_id_from_orders_table

-- Search Box (for the orders-customers web page)
-- Source: https://docs.microsoft.com/en-us/sql/relational-databases/search/full-text-search?view=sql-server-ver15
-- Source: https://stackoverflow.com/questions/14290857/sql-select-where-field-contains-words
SELECT date_time, customer_id, sale_amount, first_name, last_name, email, phone_number FROM Customers
INNER JOIN Orders ON Orders.customer_num = Customers.customer_id 
WHERE first_name LIKE :first_nameInput;

-- SELECT all employees' data to populate on the 'Employees and Managers' table
SELECT 
	CONCAT(Employees.first_name, ' ', Employees.last_name) AS Name, 
	Employees.start_date, 
	Employees.status, 
	CONCAT(Managers.first_name, ' ', Managers.last_name) AS ManagedBy, 
	Locations.city 
FROM Employees
LEFT JOIN Managers ON Managers.manager_id = Employees.emp_manager_id
LEFT JOIN Locations ON Locations.store_id = Employees.emp_store_id
ORDER BY start_date;

-- UPDATE an employee/manager's data based on edits made in the 'Employees and Managers' table
UPDATE Employees
SET 
	first_name = :first_nameInput, 
	last_name = :last_nameInput, 
	start_date = :start_dateInput, 
	status = :statusInput, 
	emp_manager_id = :emp_manager_idInput, 
	emp_store_id = :emp_store_id,
	manager_num = :manager_num

WHERE employee_id = :employee_id_from_the_table;

UPDATE Managers
SET 
	first_name = :first_nameInput,
	last_name = :last_nameInput,
	status = :statusInput,
	manager_store_id = :manager_store_idInput
WHERE CONCAT(first_name, ' ', last_name) = :employee_name_from_the_table;

-- DELETE an employee in the 'Employees and Managers' table
DELETE FROM Employees
WHERE employee_id = :employee_id_from_the_table;

DELETE FROM Managers
WHERE CONCAT(first_name, ' ', last_name) = :employee_name_from_the_table;

-- INSERT a new employee/manager data based on submission of the 'Add a new employee/manager' form
INSERT INTO Employees (first_name, last_name, start_date, status, emp_manager_id, emp_store_id)
VALUES (:first_nameInput, :last_nameInput, :start_dateInput, :emp_manager_idInput, :emp_store_idInput);

INSERT IGNORE INTO Managers (first_name, last_name, status, manager_store_id)
VALUES (:first_nameInput, :last_nameInput, :statusInput, :manager_store_idInput);

-- SELECT all store locations data to populate on the 'Locations' table
SELECT city, state, zip_code FROM Locations;

-- UPDATE a location's data based on edits made in the 'Locations' table
UPDATE Locations
SET city = :cityInput,
	state = :stateInput,
	zip_code = :zip_codeInput
WHERE store_id = :store_id_from_the_table;

-- DELETE a location in the 'Locations' table
DELETE FROM Locations
WHERE store_id = :store_id_from_the_table;

-- INSERT a new location data based on submission of the 'Add a store location' form
INSERT IGNORE INTO Locations (city, state, zip_code)
VALUES (:cityInput, :stateInput, :zip_codeInput);

