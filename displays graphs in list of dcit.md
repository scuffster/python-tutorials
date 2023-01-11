I have a python list of dictionaries like this

```
vocabs = []
dictionary={“status”:”RED”,”title”:”fijhdmdeldmirn”,”graphuri”:’<https://pid.myco.net/def/granit/>’}
vocabs.append(dictionary)
dictionary={“status”:”GREEN”,”title”:”Mandarin”,”graphuri”:’<https://pid.myco.net/def/manadribn/>’}
vocabs.append(dictionary)
dictionary={“status”:”GREEN”,”title”:”Clement”,”graphuri”:’<https://pid.myco.net/def/clement/>’}
vocabs.append(dictionary)
```

How would I pass this from my flask application to a jinja template and display it as a three column table with the column headings

“Status”, “title” and “graphuri”
In your Flask application, you can pass the list of dictionaries to the Jinja template as a variable, and then use the Jinja template to display the data in a table format.
Here's an example of how you could do this:

In your Python script:


```
from flask import render_template

@app.route("/")
def index():
    vocabs = [
        {"status":"RED","title":"fijhdmdeldmirn","graphuri":"<https://pid.myco.net/def/granit/>"},
        {"status":"GREEN","title":"Mandarin","graphuri":"<https://pid.myco.net/def/manadribn/>"},
        {"status":"GREEN","title":"Clement","graphuri":"<https://pid.myco.net/def/clement/>"},
    ]
    return render_template("index.html", vocabs=vocabs)

```

In your Jinja template(index.html):

Copy code
```
<table>
    <thead>
        <tr>
            <th>Status</th>
            <th>title</th>
            <th>graphuri</th>
        </tr>
    </thead>
    <tbody>
        {% for item in vocabs %}
            <tr>
                <td>{{ item.status }}</td>
                <td>{{ item.title }}</td>
                <td>{{ item.graphuri }}</td>
            </tr>
        {% endfor %}
    </tbody>
</table>
```
This will display the data in a table format with three columns: "Status", "title", and "graphuri", and the rows corresponding to the dictionaries in your list.




You can use the CSS property "overflow" to create a scrollable area for the table in your Jinja template. Here is an example of how you could do this:

In your Jinja template:

Copy code
```
<div style="overflow: auto; max-height: 400px;">
    <table>
        <thead>
            <tr>
                <th>Status</th>
                <th>Title</th>
                <th>Graphuri</th>
            </tr>
        </thead>
        <tbody>
            {% for item in vocabs %}
                <tr>
                    <td>{{ item.status }}</td>
                    <td>{{ item.title }}</td>
                    <td>{{ item.graphuri }}</td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
</div>
```
I wrapped the table element in a div element and set the CSS overflow property to "auto" to create a scrollable area. I also set a max-height of 400px to limit the height of the scrollable area to 400 pixels. With this in place the table will overflow if there more than 20 rows.
You can adjust the height to match your requirement.

Alternatively, you could define a CSS class to handle this behavior and apply it to the div container, so you can easily reuse the class later on other parts of the website and maintain a consistent look.


To add a scrollbar to the scrollable area, you can add the property overflow-y:scroll; to the CSS that controls the div element that wraps the table. This will create a scrollbar on the y-axis (vertically) of the div element and allow the user to scroll through the content inside it.

Here's an example of how you could add this property to the CSS class:

Copy code
```
<style>
    .scrollable {
        overflow: auto;
        max-height: 400px;
        overflow-y:scroll; /* This will add a scrollbar */
    }
</style>

<div class="scrollable">
    <table>
        <thead>
            <tr>
                <th>Status</th>
                <th>Title</th>
                <th>Graphuri</th>
            </tr>
        </thead>
        <tbody>
            {% for item in vocabs %}
                <tr>
                    <td>{{ item.status }}</td>
                    <td>{{ item.title }}</td>
                    <td>{{ item.graphuri }}</td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
</div>
```
You can also add scrollbar for x-axis (horizontally) by adding overflow-x:scroll;

Copy code
```
.scrollable {
        overflow: auto;
        max-height: 400px;
        overflow-y:scroll; 
        overflow-x:scroll; /* This will add a horizontal scrollbar */
    }
```

Keep in mind that the exact appearance of the scrollbar will depend on the operating system and browser being used. Some browsers, like Mozilla Firefox, and Internet explorer allow customizing the appearance of the scrollbar through CSS, but not all browsers support these properties so you will want to test the behavior of your website on different browsers to ensure compatibility.




