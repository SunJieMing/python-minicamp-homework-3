# Homework #3

## Instructions
---
1. Create a project folder.  Setup your virtual environment.  Install `flask`.

2. Create a `/templates` folder in your project directory with the following `html` templates.
	
    *home.html*
    ```
    <img src="https://lambdaschool.com/static/assets/images/lambda.png">
    <h1>Food Database</h1>
    <h3><a href="/enternew">Add Food</a></h3>
    <br>
    <br>
    <br>
    <h3>Apply now for a chance to attend one of our immersive programs beginning in April 2017.</h3>
    <p>Our immersive programs combine small class sizes, world class instructors, a curriculum comprised of cutting edge technologies, and career counseling to help you begin a successful career as a software engineer.  All at a fraction of the cost of a traditional Computer Science degree.</p>
    <h4>Our curriculum includes:</h4>
    <ul>
        <li>Computer science fundamentals including data structures, algorithms, complexity analysis, and an intro to data science</li>
        <li>Front-end web development using HTML, CSS/SASS, React, Redux, and client testing  </li>
        <li>Back-end development including Node/Express, MySQL, MongoDB, Redis, auth/security, devops, server testing, and more </li>
        <li>An introduction to mobile development using React Native</li>
        <li>Agile Development, Test Driven Development</li>
        <li>Interviewing strategies, resume writing, and how to leverage social media and other online resources to help you find the right job</li>
        <li>Long-term career strategies and how to position yourself to not just find a job but to create a successful and lucrative career as a software engineer</li>
    </ul>
    <h4>For more information click <a href="https://lambdaschool.com">HERE</a>.</h4>

    ```
    *food.html*
    ```
    <form action = "{{ url_for('addfood') }}" method = "POST">
      <h3>Food Info</h3>
      Name<br>
      <input type = "text" name = "name" /></br>
      Calories<br>
      <textarea name = "calories" ></textarea><br>
      Cuisine<br>
      <input type = "text" name = "cuisine" /><br>
      Vegetarian<br>
      <input type = "text" name = "is_vegetarian" /><br>
      Gluten Free<br>
      <input type = "text" name = "is_gluten_free" /><br>
      <input type = "submit" value = "submit" /><br>
	</form>
    ```
    
    *result.html*
    ```
    <h1>result of addition : {{ message }}</h1>
	<h2><a href = "/">Home</a></h2>
    ```

3. Initialize your database.  Create a file called `initdb.py`.  Copy the contents shown below into `initdb.py`.  Run `initdb.py` with this command: `Python initdb.py`.  After running this script a file called `database.db` is created.  This is your `SQLite3` database.  `SQLite3` reads and writes to a single static file without needing a separate database server running locally.

	*initdb.py*
    ```
    import sqlite3

    connection = sqlite3.connect('database.db')
    print 'Opened database successfully';

    connection.execute('CREATE TABLE foods (name TEXT, calories TEXT, cuisine TEXT, is_vegetarian TEXT, is_gluten_free TEXT)')
    print 'Table created successfully';
    
    connection.close()
	```

4. Create your server file, import the needed dependencies, and create the home route (`/`).  This route should render the `home.html` template.  Start your server and go to `localhost:5000/`. Your file structure should now look like this:
    ```
       project-name/
       --server.py (or whatever you named your python script)
       --initdb.py
       --database.db
       --templates/
       ---- home.html
       ---- food.html
       ---- result.html
       --venv/
    ```
    
5. Implement the `/enternew` route.  This route should simply render `food.html`.


6. Implement the `/addfood` route.  This route should accept a `POST` request.  This route should accept the form data sent from the `food.html` template and `INSERT` it into the database.  Use the lecture code as a reference.  Verify that you are correctly inserting the data into the database by uploading your `database.db` file to http://inloop.github.io/sqlite-viewer/.


---

### Extra Credit

1. Create a route called `/favorite` that queries the database for your favorite food and returns it as `JSON`.  Hard code the query string, it doesn't need to be dynamically built from a route parameter.  For example, `'SELECT * FROM foods WHERE name = "mango"'`.  Make sure this food already exists inside of your database.  Add a link to this route on your home page.

2. Create a route called `/search`.  Add the search form below to your `home.html` file below the food database header.  `/search` should accept a `GET` request and then access the query parameter `name` and use that to perform a `SELECT` query on the database for any row that has a matching `name` field.  Return the results as `JSON`.

	```
    <form action="{{ url_for('search') }}" method="GET">
        <h3>Search</h3>
        <input type="text" name="name" />
        <input type="submit" />
    </form>
	```

3. Create a route called `/drop`.  This route should drop the table `foods`.  Return the string `'dropped'` after successfully dropping the table.  This wipes out the `foods` table so all of your routes will be nonfunctional until you run the `initdb.py` script again.

---
#### Congratulations on finishing Homework #3!
Apply to our full time or part time immersive program to learn cutting edge technologies that are used by top technology companies around the world.

Our part time and full time courses are 13 intense weeks of focused study on the most relevant technologies.  

Class sizes are small to ensure that each student gets individual attention from our world class instructors to help them succeed.

For more information visit: https://lambdaschool.com
