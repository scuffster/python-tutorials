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