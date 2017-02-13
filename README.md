# Homework #3

## Instructions
---

1. Create a `/templates` folder with the following `html` templates.\
	*home.html*
    ```
    <!DOCTYPE html>
    <img src="https://lambdaschool.com/static/assets/images/lambda.png">
    <h1>Food Database</h1>
    <form action="{{ url_for('search') }}" method="GET">
        <h3>Search</h3>
        <input type="text" name="name" />
        <input type="submit" />
    </form>
    <h3><a href="/enternew">Add Food</a></h3>
    <h3><a href="/list">Show Foods</a></h3>
    <h3><a href="/favorite">Favorite Food</a></h3>
    <br>
    <br>
    <br>
    <h3>Apply now for a chance to attend one of our immersive programs beginning in April 2017.</h3>
    <p>Our immersive programs combine small class sizes, world class instructors, a curriculum comprised of cutting edge technologies, and career counseling to help you begin a successful career as a software engineer.  All at a fraction of the cost of a traditional Computer Science degree.</p>
    <h4>Our curriculum includes:</h4>
    <ul>
      <li>Computer science fundamentals including data structures, algorithms, complexity analysis, an intro to data science, and more</li>
      <li>Front-end web development using HTML, CSS/SASS, React, Redux, client testing, and more  </li>
      <li>Back-end development including Node/Express, MySQL, MongoDB, Redis, auth/security, devops, server testing, and more </li>
      <li>An introduction to mobile development using React Native</li>
      <li>Agile development</li>
      <li>Interviewing strategies, resume writing, and how to leverage social media and other online resources to help you find the right job</li>
      <li>Long-term career strategies and how to position yourself to not just find a job but to create a successful and lucrative career as a software engineer</li>
    </ul>

    ```
    *food.html*
    ```
    <form action = "{{ url_for('addrecord') }}" method = "POST">
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
    
    *list.html*
    ```
    <table border = 1>
      <thead>
        <td>Name</td>
        <td>Calories</td>
        <td>Cuisine</td>
        <td>Vegetarian</td>
        <td>Gluten Free</td>
      </thead>

      {% for row in rows %}
      <tr>
        <td>{{row["name"]}}</td>
        <td>{{row["calories"]}}</td>
        <td>{{row['cuisine']}}</td>
        <td>{{row['is_vegetarian']}}</td>
        <td>{{row['is_gluten_free']}}</td>
      </tr>
      {% endfor %}
	</table>

	<a href = "/">Home</a>
	```
    
    *result.html*
    ```
    <h1>result of addition : {{ message }}</h1>
	<h2><a href = "/">go back to home page</a></h2>
	<h2><a href = "/list">See Food List</a></h2>
    ```

2. Build a route called `/birthday` that returns your birthday as a `string` in this format: `'October 30 1911'`.

	***Example***: A GET request to `localhost:5000/birthday` returns `'October 30 1911'` (Use your birthday instead)


3. Build a route called `/greeting` that accepts a parameter called `name`.  The route should return a string
that says `'Hello <name>'` where `<name>` is the name that you passed to the route.  

	***Example***: A GET request to `localhost:5000/greeting/ben` would return 'Hello ben!'
    
4. Modify your home route (`/`) to return the html template provided below.
	* Create a folder called `templates` in the root of your project's directory.
	* Create a file called `home.html` in the templates directory.
	* Paste the HTML shown below into `home.html` and save.
	* In your main server file modify the `flask` import line to say: `from flask import Flask, render_template`
	* In your home (`/`) route `return render_template('home.html')`.
	* Navigate to `localhost:5000/` and you should see the rendered HTML.
	
Your file structure should look like this:
```
 project-name/
 --server.py (or whatever you named your python script)
 --templates/
 ---- home.html
 --venv/
```
    
Paste this HTML into `home.html`.

```
<!DOCTYPE html>
<html>
  <body>
    <img src="https://lambdaschool.com/static/assets/images/lambda.png">
    <h1>Congrats!</h1>
    <h3>You just served your first webpage.</h3>
    <p>This page is pretty bare right now but these are the fundamentals that all websites are built on.  Later in the course we will teach you some basic HTML, CSS, and Javascript so that you can structure more sophisticated pages with more detailed designs and complex functionality</p>
    <p>Our full time and part time courses will go much more in depth as to what it takes to build the same kinds of web applications that you know and love.  We will be covering the cutting edge frameworks used by industry leaders to create highly performant and beautiful applications.</p>
  </body>
</html>
```
---

### Extra Credit

1. Create a route called `/add` that adds two parameteres together and returns them.
	* `localhost:5000/add/5/10` would return `'15'`
	* You will need to convert the parameters to integers using `int()`
	* Example: `fiveAsInt = int('5')` => `fiveAsInt == 5`
	* You then have to convert the `int` back into a `string` using `str()`
	* Example: `fiveAsString = str(5)` => `fiveAsString == '5'`
	* You can also prefix the parameter with the keyword `int` => `<int:param>`. Make sure you turn it back into a `string`

2. Create a route called `/multiply` and a route called `/subtract` 
	* `localhost:5000/multiply/6/5` would return `'30'`
	* `localhost:5000/subtract/25/5` would return `'20'`
	* Make sure you are converting the parameters to `int`s and returning a `string`

3. Create a route called `/favoritefoods` that returns a `list` of your favorite foods
	* A `list` is a collection of different values. => `['football', 'basketball', 'rugby']`
	* The server must return a string so we need to convert our list into a string.
	* One common string format for sending complex data is `JSON`.
	* Change the top line of your server file to `from flask import Flask, render_template, jsonify`
	* Pass your `list` to `jsonify()` when returning it. `return jsonify(myList)`

---
#### Congratulations on finishing Homework #2
Apply to our full time or part time immersive program to learn cutting edge technologies that are used by top technology companies around the world.

Our part time and full time courses are 13 intense weeks of focused study on the most relevant technologies.  

Class sizes are small to ensure that each student gets individual attention from our world class instructors to help them succeed.

For more information visit: https://lambdaschool.com
