import psycopg2
from psycopg2 import Error

db_url = "postgresql://nicole:WDqvmEuTJIlG2KRzYrTX3Q@shaded-dove-6942.5xj.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dshaded-dove-6942"
connection = psycopg2.connect(db_url)
cursor = connection.cursor()

def create_table():
    try:

        delete = "DROP TABLE IF EXISTS foods"
        delete2 = "DROP TABLE IF EXISTS food_ingredients"
        create_query = "CREATE TABLE foods (id INT PRIMARY KEY, name STRING, sellable INT, selling_price INT, perishable INT, time_to_spoil INT, known INT)"
        create_query2 = "CREATE TABLE food_ingredients (id INT PRIMARY KEY, ingredient1 INT, ingredient2 INT, ingredient3 INT, height INT)"
        cursor.execute(delete)
        cursor.execute(delete2)
        cursor.execute(create_query)
        cursor.execute(create_query2)

        connection.commit()
        print("Table successfully created! :D")

    except (Exception, Error) as error:
        print("Error creating table: \n ", error)

def insert_foods(id, name, sellable, selling_price, perishable, time_to_spoil, known):
    delete_foods(id)
    insert_query = "INSERT INTO foods (id, name, sellable, selling_price, perishable, time_to_spoil, known) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (str(id), str(name), str(sellable), str(selling_price),
                                                                              str(perishable), str(time_to_spoil),
                                                                                                        str(known))
    cursor.execute(insert_query)

def delete_foods(id):
    delete_query = "DELETE FROM foods where id=%s" %(str(id))
    cursor.execute(delete_query)

def insert_ingredients(id, ingredient1, ingredient2, ingredient3, height):
    delete_ingredients(id)
    insert_query = "INSERT INTO food_ingredients(id, ingredient1, ingredient2, ingredient3, height) VALUES (%s, %s, %s, %s, %s )" \
                   % (str(id), str(ingredient1), str(ingredient2), str(ingredient3), str(height))
    cursor.execute(insert_query)

def delete_ingredients(id):
    delete_query = "DELETE FROM food_ingredients where id=%s" % (str(id))
    cursor.execute(delete_query)

def display():
    select_query = "SELECT * FROM food_ingredients"
    cursor.execute(select_query)
    print(cursor.fetchall())

def select_recipe(ingredient1, ingredient2):
    array = [0, ingredient1, ingredient2]
    array.sort()
    select_query = "SELECT foods.id, name, sellable, selling_price, perishable, time_to_spoil, known FROM foods JOIN food_ingredients ON foods.id=food_ingredients.id WHERE ingredient1 = %s and ingredient2 = %s and ingredient3 = %s " \
                   % (str(array[0]), str(array[1]), str(array[2]))
    cursor.execute(select_query)
    print(cursor.fetchall())


create_table()
insert_foods(1, "pan", 0, 0, 0, 0, 1)
insert_foods(2, "oven", 0, 0, 0, 0, 1)
insert_foods(3, "wheat", 1, 1, 1, 30, 1)
insert_foods(4, "sugarcane", 1, 1, 1, 30, 1)
insert_foods(5, "corn", 1, 1, 1, 30, 1)
insert_foods(6, "tomato", 1, 1, 1, 30, 1)
insert_foods(7, "bread", 1, 1, 1, 30, 1)
insert_foods(8, "sauce", 1, 1, 1, 30, 1)
insert_foods(9, "pasta", 1, 1, 1, 30, 1)
insert_foods(10, "spaghetti", 1, 1, 1, 30, 1)
insert_foods(11, "water", 1, 1, 1, 30, 1)
insert_foods(12, "eggs", 1, 1, 1, 30, 1)
insert_foods(13, "flour", 1, 1, 1, 30, 1)
insert_foods(14, "corn flour", 1, 1, 1, 30, 1)
insert_foods(15, "cornbread ", 1, 1, 1, 30, 1)

insert_ingredients(1, 0, 0, 0, 1)
insert_ingredients(2, 0, 0, 0, 1)
insert_ingredients(3, 0, 0, 0, 1)
insert_ingredients(4, 0, 0, 0, 1)
insert_ingredients(5, 0, 0, 0, 1)
insert_ingredients(6, 0, 0, 0, 1)
insert_ingredients(7, 0, 11, 13, 2)
insert_ingredients(8, 0, 1, 6, 2)
insert_ingredients(9, 0, 12, 13, 2)
insert_ingredients(10, 0, 8, 9, 3)
insert_ingredients(11, 0, 0, 0, 1)
insert_ingredients(12, 0, 0, 0, 1)
insert_ingredients(13, 0, 0, 0, 1)
insert_ingredients(14, 0, 0, 0, 1)
insert_ingredients(15, 0, 11, 14, 2)
