# Python Server Side Rendering Tasks

### Task Summary

#### Task 0: Creating a Simple Templating Program
- **Objective**: Understand string templating in Python, implement file operations, and handle edge cases.
- **Instructions**:
  - Create a Python function `generate_invitations` that takes a template string and a list of attendees.
  - Verify input types and handle empty inputs.
  - Replace placeholders in the template with actual values from the attendees' data.
  - Generate output files named `output_X.txt`, where X is the index of the attendee.
  - Implement specific error handling for various edge cases.

#### Task 1: Creating a Basic HTML Template in Flask
- **Objective**: Set up a Flask environment, design HTML templates using Jinja, and implement reusable components.
- **Instructions**:
  - Set up a Flask environment and create a basic Flask application.
  - Design an HTML template `index.html` with headings, paragraphs, and lists.
  - Create reusable header and footer templates.
  - Design additional pages (`about.html`, `contact.html`) with shared header and footer.
  - Add routes in the Flask application for the new pages.

#### Task 2: Creating a Dynamic Template with Loops and Conditions in Flask
- **Objective**: Use Jinja’s loop and conditional constructs to dynamically render content.
- **Instructions**:
  - Create a dynamic template `items.html` to display a list of items.
  - Use a JSON file `items.json` to provide the list of items.
  - Add a route `/items` in the Flask application to render the template with the list of items.
  - Implement conditional statements to display a message if the list is empty.

#### Task 3: Displaying Data from JSON or CSV Files in Flask
- **Objective**: Read and parse data from JSON and CSV files, use query parameters, and handle edge cases.
- **Instructions**:
  - Create JSON and CSV files with product data.
  - Design a dynamic template `product_display.html` to display product data.
  - Modify the Flask application to read and parse data from JSON or CSV files based on a query parameter.
  - Implement error handling for invalid inputs and missing data.

#### Task 4: Extending Dynamic Data Display to Include SQLite in Flask
- **Objective**: Set up and interact with a SQLite database, extend functionality to handle multiple data sources.
- **Instructions**:
  - Set up a SQLite database with a Products table.
  - Extend the existing Flask route to handle `source=sql` as a query parameter.
  - Implement logic to fetch data from the SQLite database.
  - Use the same template `product_display.html` to display data regardless of the source.
  - Handle error cases for invalid sources and database-related issues.

### Resources
- **Python String Methods**: [Python Official Documentation](https://docs.python.org/3/library/stdtypes.html#string-methods)
- **File Handling in Python**: [Python Official Documentation](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- **Flask Quickstart**: [Flask Quickstart](https://flask.palletsprojects.com/en/2.0.x/quickstart/)
- **HTML Basics**: [HTML Tutorial on W3Schools](https://www.w3schools.com/html/)
- **Flask Templating with Jinja**: [Flask Templating](https://flask.palletsprojects.com/en/2.0.x/templating/)
- **Jinja Template Inheritance**: [Jinja Template Inheritance](https://jinja.palletsprojects.com/en/3.0.x/templates/#template-inheritance)
- **Reading JSON and CSV in Python**: [JSON in Python](https://docs.python.org/3/library/json.html), [CSV File Reading and Writing](https://docs.python.org/3/library/csv.html)
- **Flask Request Object**: [Flask Request Object](https://flask.palletsprojects.com/en/2.0.x/api/#flask.Request)
- **Error Handling in Flask**: [Flask Error Handling](https://flask.palletsprojects.com/en/2.0.x/errorhandling/)
- **Flask-SQLAlchemy**: [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- **SQLite in Python**: [SQLite3 Module](https://docs.python.org/3/library/sqlite3.html)
