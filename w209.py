"""
06/27/2024. Experimenting with adding Javascript to w209.py file
Took elements of javascript to copy over.

This is from the prior documentation (week 8):
- Example of writing JSON format graph data and using D3 JavaScript library to produce an HTML/JavaScript drawing.
- You will need to download the following directory:
- https://github.com/networkx/networkx/tree/main/examples/external/force

"""

from flask import Flask, render_template

# Serve the file over http to allow for cross origin requests
app = Flask(__name__, static_folder="force")

import pandas as pd

#new
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

@app.route("/")
def w209():
    file="about9.jpg"
    return render_template("w209.html",file=file)

@app.route("/pandas-api/")
def api():
    d = pd.DataFrame([{"a":"b"}])
    return d.to_dict()

@app.route("/test_sn/")
def test():
    file = "REACT_summary.png"
    return render_template("test_sn.html", file = file), 200, {'header-a': 'b'} 

@app.route("/test_sn2/")
def static_proxy():
#    return render_template("force.html")
   return app.send_static_file("force.html")

if __name__ == "__main__":
    app.run(port=8000)

