how do I query the list of named graphs in a fuseki instance using python, then display the list in a jinja2 template?

To query the list of named graphs in a Fuseki instance using Python, you can use the following SPARQL query:

```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT DISTINCT ?graph
WHERE {
    GRAPH ?graph { ?s ?p ?o }
}
```

This query will select the names of all the named graphs in the Fuseki instance that contain at least one triple.

To run this query and display the list of named graphs in a Jinja template, you can use the following code in your Python code:

```
from SPARQLWrapper import SPARQLWrapper, JSON
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # Set the endpoint URL
    sparql = SPARQLWrapper("http://your-fuseki-server:3030/skosmos/query")

    # Set the query string
    query = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

    SELECT DISTINCT ?graph
    WHERE {
        GRAPH ?graph { ?s ?p ?o }
    }
    """

    # Set the query format to JSON
    sparql.setReturnFormat(JSON)

    # Set the query
    sparql.setQuery(query)

    # Send the query and get the results
    results = sparql.query().convert()

    # Extract the list of graph names from the results
    graph_names = [result["graph"]["value"] for result in results["results"]["bindings"]]

    # Render the template with the list of graph names
    return render_template("template.html", graph_names=graph_names)


```

Then, in your Jinja template file template.html, you can use a loop to print the list of graph names as follows:

```
<ul>
    {% for graph_name in graph_names %}
    <li>{{ graph_name }}</li>
    {% endfor %}
</ul>
```

This will render the template.html file with a list of the names of the named graphs in the Fuseki instance.

Note: You will need to install the SPARQLWrapper and flask packages using pip install SPARQLWrapper flask. You may also need to replace "http://your-fuseki-server:3030/skosmos/query" with the actual URL of your SPARQL endpoint





