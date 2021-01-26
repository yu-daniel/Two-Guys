from flask import Flask, request, render_template
from forms import IngredientsForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f3dc1ba89e01d2f814d04deb20db5e7c'
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
@app.route('/')
def root():
    return render_template("index.html")


# route for the ingredients & suppliers page
@app.route("/ingredients-suppliers", methods=["GET", "POST"])
def ingredients_suppliers():
    form = IngredientsForm()
    return render_template("ingredients_suppliers.html", title='Register', form=form,
                           column_headers=column_headers, sample_values=sample_values)




if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3001))
    app.run(port=port, debug=True)
