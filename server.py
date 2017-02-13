from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def new_food():
       return render_template('food.html')

@app.route('/addfood', methods = ['POST'])
def addfood():
    #initialize the connection and cursor
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    #prep the values that will be inserted
    name = request.form['name']
    calories = request.form['calories']
    cuisine = request.form['cuisine']
    isVegetarian = request.form['is_vegetarian']
    isGlutenFree = request.form['is_gluten_free']

    try:
        #insert the new food item
        cursor.execute('INSERT INTO foods(name, calories, cuisine, is_vegetarian, is_gluten_free) VALUES (?, ?, ?, ?, ?)', (name, calories, cuisine, isVegetarian, isGlutenFree))
        connection.commit()
        message = 'Record successfully added'
    except:
        message = 'Error on insert operation'
        conection.rollback()
    finally:
        #display the insert result
        return render_template('result.html', message = message)
        connection.close()

@app.route('/list')
def list():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute('SELECT * from foods')

    rows = cursor.fetchall()
    connection.close()
    return render_template('list.html', rows = rows)

@app.route('/favorite')
def favorite():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM foods WHERE name = \'steak\'')
    favoriteFood = cursor.fetchall()[0]
    connection.close();
    return jsonify(favoriteFood);

@app.route('/search')
def search():
    name = request.args.get('name')
    dbQuery = 'SELECT * FROM foods WHERE name = "' + name + '"'
    connection = sqlite3.connect('database.db')

    cursor = connection.cursor()
    cursor.execute(dbQuery)

    favoriteFood = cursor.fetchall()
    connection.close();

    return jsonify(favoriteFood);

@app.route('/drop')
def drop():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('DROP TABLE foods')
    connection.commit()
    connection.close()
    return 'dropped'


if __name__ == '__main__':
   app.run(debug = True)
