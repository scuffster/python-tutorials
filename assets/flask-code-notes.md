Python code that you can use to create a navigation bar in a Flask application with a file upload page using Jinja templates:

```
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return 'file uploaded successfully'

if __name__ == '__main__':
    app.run()
```

To create the navigation bar in your Jinja template, you can use the following code:
```
<nav>
  <ul>
    <li><a href="{{ url_for('index') }}">Home</a></li>
    <li><a href="{{ url_for('about') }}">About</a></li>
    <li><a href="{{ url_for('upload') }}">Upload</a></li>
    <li><a href="{{ url_for('contact') }}">Contact</a></li>
  </ul>
</nav>
```

This will create a simple navigation bar with four links: "Home", "About", "Upload", and "Contact". When a user clicks on the "Upload" link, they will be redirected to the file upload page.

To create the file upload page, you can use the following code in your Jinja template:

```
<form action = "{{ url_for('upload_file') }}" method = "POST" enctype = "multipart/form-data">
   <input type = "file" name = "file" />
   <input type = "submit"/>
</form>
```
This will create a simple file upload form that allows users to select a file to upload. When the form is submitted, the file will be uploaded to the server and the message "file uploaded successfully" will be displayed.

how do I include the navigation bar in each ninja template?

To include the navigation bar in each Jinja template, you can use an extend block in your base template, and then include the navigation bar in the base template using a block. Here is an example of how you can do this:

First, create a base template called base.html that includes the navigation bar and a block for the content of your pages:

```
<html>
  <head>
    <title>{% block title %}{% endblock %}</title>
  </head>
  <body>
    <nav>
      <ul>
        <li><a href="{{ url_for('index') }}">Home</a></li>
        <li><a href="{{ url_for('about') }}">About</a></li>
        <li><a href="{{ url_for('upload') }}">Upload</a></li>
        <li><a href="{{ url_for('contact') }}">Contact</a></li>
      </ul>
    </nav>
    {% block content %}{% endblock %}
  </body>
</html>

```

Then, in each of your other templates (e.g. index.html, about.html, etc.), you can use the extend block to inherit from the base template and define the content of each page:

```
{% extends "base.html" %}
{% block title %}Home{% endblock %}
{% block content %}
  <h1>Welcome to the Homepage!</h1>
  <p>Here is some content for the homepage.</p>
{% endblock %
}
```
```
{% extends "base.html" %}
{% block title %}About{% endblock %}
{% block content %}
  <h1>About Us</h1>
  <p>Here is some information about our company.</p>
{% endblock %}

```
This way, you can include the navigation bar in every template without having to copy and paste the code into each template. Instead, you can simply define the navigation bar in the base template and then use the extend block to include it in all of your other templates.


how do I show the nav bar horizontally at the top in the base html template? 
To show the navigation bar horizontally at the top of the base template, you can add some CSS styles to the <nav> element. Here is an example of how you can do this:

```
<html>
  <head>
    <title>{% block title %}{% endblock %}</title>
    <style>
      nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
      }
      nav ul {
        list-style: none;
        display: flex;
      }
      nav ul li {
        margin: 0 10px;
      }
      nav ul li a {
        text-decoration: none;
        color: black;
      }
    </style>
  </head>
  <body>
    <nav>
      <ul>
        <li><a href="{{ url_for('index') }}">Home</a></li>
        <li><a href="{{ url_for('about') }}">About</a></li>
        <li><a href="{{ url_for('upload') }}">Upload</a></li>
        <li><a href="{{ url_for('contact') }}">Contact</a></li>
      </ul>
    </nav>
    {% block content %}{% endblock %}
  </body>
</html>

```

This will apply the following styles to the navigation bar:

display: flex: This will make the navigation bar a flex container, allowing you to align the items horizontally.
justify-content: space-between: This will distribute the space evenly between the items, with the first and last items aligned with the edges of the container.
align-items: center: This will align the items vertically in the center of the container.
list-style: none: This will remove the default bullet points from the list items.
display: flex: This will make the list items into flex items, allowing you to align them horizontally.
margin: 0 10px: This will add a 10px margin to the left and right of each list item.
This will result in a navigation bar that is displayed horizontally at the top of the page, with the items evenly spaced and aligned in the center.


what does the extend block look like for the upload template?
To use the extend block in the upload.html template, you would write something like this:

```
{% extends "base.html" %}
{% block title %}Upload{% endblock %}
{% block content %}
  <h1>Upload a File</h1>
  <form action = "{{ url_for('upload_file') }}" method = "POST" enctype = "multipart/form-data">
    <input type = "file" name = "file" />
    <input type = "submit"/>
  </form>
{% endblock %}

```

This will inherit the base template and define the content of the upload page. The {% block title %} and {% block content %} blocks will override the corresponding blocks in the base template with the content specified in the upload template.

how do I place the nav items in a blue header in the base.html template?
To place the navigation bar items in a blue header in the base template, you can add a <header> element around the <nav> element and apply a blue background color to the header. Here is an example of how you can do this:

```
<html>
  <head>
    <title>{% block title %}{% endblock %}</title>
    <style>
      header {
        background-color: blue;
      }
      nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
      }
      nav ul {
        list-style: none;
        display: flex;
      }
      nav ul li {
        margin: 0 10px;
      }
      nav ul li a {
        text-decoration: none;
        color: white;
      }
    </style>
  </head>
  <body>
    <header>
      <nav>
        <ul>
          <li><a href="{{ url_for('index') }}">Home</a></li>
          <li><a href="{{ url_for('about') }}">About</a></li>
          <li><a href="{{ url_for('upload') }}">Upload</a></li>
          <li><a href="{{ url_for('contact') }}">Contact</a></li>
        </ul>
      </nav>
    </header>
    {% block content %}{% endblock %}
  </body>
</html>
```
This will add a blue header around the navigation bar and change the color of the links to white. You can adjust the background color and link color to your liking by changing the values of the background-color and color properties in the CSS styles.
