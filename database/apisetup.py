import flask
import psycopg2
from flask import request, jsonify

db_url = "postgresql://nicole:WDqvmEuTJIlG2KRzYrTX3Q@shaded-dove-6942.5xj.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dshaded-dove-6942"
connection = psycopg2.connect(db_url)
cursor = connection.cursor()

def dict_factory(vCursor, row):
    d = {}
    for idx, col in enumerate(vCursor.description):
        d[col[0]] = row[idx]
    return d

connection = psycopg2.connect(db_url)
cursor = connection.cursor()

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>API for reaching the food database</h1>"


@app.route('/api/v1/allfoods')
def api_all_foods():
    cursor.execute("SELECT * FROM foods")
    all_foods = cursor.fetchall()
    print(all_foods)
    return jsonify(all_foods)

@app.route('/api/vi/find_recipe/<ingredient1>/<ingredient2>/<appliance>')
def api_recipe(ingredient1, ingredient2, appliance):
    array = [0, ingredient1, ingredient2]
    array.sort()
    select_query = "SELECT foods.id, name, sellable, selling_price, perishable, time_to_spoil, known FROM foods JOIN food_ingredients ON foods.id=food_ingredients.id WHERE ingredient1 = %s and ingredient2 = %s and ingredient3 = %s and appliance = %s" \
                   % (str(array[0]), str(array[1]), str(array[2]), str(appliance))
    cursor.execute(select_query)
    recipe = cursor.fetchone()
    return jsonify(recipe)

@app.route('/api/v1/get_name/<id>')
def get_name_by_id(id):
    query = "SELECT foods.name from foods where foods.id=%s" % (str(id))
    cursor.execute(query)
    item = cursor.fetchone()
    return jsonify(item)

app.run()
