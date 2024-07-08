"""
==========
JavaScript
==========

Example of writing JSON format graph data and using the D3 JavaScript library
to produce an HTML/JavaScript drawing.

You will need to download the following directory:

- https://github.com/networkx/networkx/tree/main/examples/external/force
"""
import json

import flask
import networkx as nx

G = nx.florentine_families_graph()
# this d3 example uses the name attribute for the mouse-hover value,
# so add a name to each node
for n in G:
    G.nodes[n]["name"] = n

communities = list(nx.community.label_propagation_communities(G))
centralities = nx.eigenvector_centrality(G)

for f in G.nodes():
	for i, c in enumerate(communities):
        	if f in c:
            		G.nodes[f].update({"community" : str(i),
                        	        "centrality" : centralities[f],
                                	"name" : f
                               })

# write json formatted data
d = nx.json_graph.node_link_data(G)  # node-link format to serialize
# write json
json.dump(d, open("force/force.json", "w"))
print("Wrote node-link JSON data to force/force.json")

# Serve the file over http to allow for cross origin requests
app = flask.Flask(__name__, static_folder="force")


@app.route("/")
def static_proxy():
    return app.send_static_file("force.html")


print("\nGo to http://localhost:8000 to see the example\n")
app.run(port=8000)
