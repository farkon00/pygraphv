# Pygraphv

__Pygraphv__ - python library for generating dot programming language for creating graphviz graphs from python OO style code.

# Examples
Basic graph:
```py
from pygraphv.graph import Graph
from pygraphv.node import Node
from pygraphv.style import GraphStyle

# Chose one of this
# You can look at difference in Graphviz docs
# digraph = Digraph("Digraph")
graph = Graph("Graph")

# Adds node with name A, that has child node B
a = Node("A")
graph.add_node(a)
graph.add_node(Node("B"), parent=a)

# Generates .dot file for your graph and saves it in "Your first graph.dot"
# And renders it to svg file, needs dot compiler installed and added to path
graph.render("Your first graph")
```

<img src="https://github.com/farkon00/pygraphv/blob/master/examples/basic.svg">

Styles:
```py
from pygraphv.graph import Digraph
from pygraphv.style import *
from pygraphv.node import Node

# Now digraph example
# Only difference to regular graph is arrows at ends of connections
graph = Digraph("Graph", styles=[GraphStyle(bgcolor="lightblue"), GraphStyle(href="github.com/farkon00")])

# Adds node with name A, that has child node B
a = Node("A", styles=NodeStyle(color="red", shape="box"))
graph.add_node(a)
graph.add_node(Node("B"), label="Styled edge", parent=a, styles=EdgeStyle(arrowhead="box"))

# Generates .dot file for your graph and saves it in "Styles.dot"
# And renders it to svg file, needs dot compiler installed and added to path
graph.render("Styles")
```

<img src="https://github.com/farkon00/pygraphv/blob/master/examples/styles.svg">

Clusters:
```py
from pygraphv.graph import Graph, Cluster
from pygraphv.style import *
from pygraphv.node import Node

graph = Graph("Graph")

# Adds node with name A, that has child node B
a = Node("A")
graph.add_node(a)
graph.add_node(Node("B"), parent=a)

# Creates cluster and adds cycle of 3 nodes, connected to node A

# Can be compressed to one style object
# But you can use GraphStyle on clusters
cluster = Cluster("Cluster", styles=(GraphStyle(bgcolor="lightgreen"), ClusterStyle(style="dotted")))

node1 = Node("1")
cluster.add_node(node1)
a.children.append(node1)
cluster.add_node(Node("2"), parent=node1)
cluster.add_node(Node("3"), parent=node1)
graph.add_node(node1.children[-1].node, parent=node1.children[-2].node)

graph.add_subgraph(cluster)

# Generates .dot file for your graph and saves it in "Clusters.dot"
# And renders it to svg file, needs dot compiler installed and added to path
graph.render("Clusters")
```

<img src="https://github.com/farkon00/pygraphv/blob/master/examples/clusters.svg">