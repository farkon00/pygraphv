"""
Graph module for graph and digraph classes
"""

import subprocess

from .node import Node

class Graph:
    """
    Base class for graphs in the pygraphv library.

    Can generate dot code for the graph.
    """

    GRAPH_TYPE = "graph"
    SEPARATOR = "--"

    def __init__(self, name: str = "Graph"):
        """
        Base class for graphs in the pygraphv library.

        Can generate dot code for the graph.
        """

        self.name = name
        self.nodes = []

    def add_node(self, node: Node, parent: Node = None):
        """
        Adds a node to the graph or child node if parent is provided. 
        """
        if parent is None:
            self.nodes.append(node)
            return
        parent.children.append(node)

    def generate(self, fp: str = None) -> str | None:
        """
        Generates dot code for the graph.

        If fp is None, returns dot code.
        """
        buf = ""
        generated = []

        buf += f"{self.GRAPH_TYPE} {self.name}" + " {\n"

        for i in self.nodes:
            buf += i.generate(generated=generated, sep=self.SEPARATOR)

        buf += "}\n"

        if fp is None:
            return buf
        else:
            with open(fp, "w") as output:
                output.write(buf)

    def render(self, file_name: str, save_dot: bool = True):
        """
        Generates dot code for the graph and renders it with dot.

        Throws an error if dot is not installed.

        File name should be without extension.

        If save_dot is false, .dot output file will be deleted.
        """
        self.generate(fp=f"{file_name}.dot")
        
        subprocess.run(["dot", f"{file_name}.dot", "-Tsvg", "-o", f"{file_name}.svg"])

        if not save_dot:
            subprocess.run([f"rm {file_name}.dot"])

class Digraph(Graph):
    """
    Class for digraphs in the pygraphv library.

    Can generate dot code for the graph.
    """

    GRAPH_TYPE = "digraph" 
    SEPARATOR = "->"