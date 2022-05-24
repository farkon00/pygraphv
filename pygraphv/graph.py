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
    
    # Actual generate function, there is wrapper for drying the code
    def _generate(self, fp: str = None, sep: str = "--", graph: str = "graph") -> str | None:
        buf = ""
        generated = []

        buf += f"{graph} {self.name}" + " {\n"

        for i in self.nodes:
            buf += i.generate(generated=generated, sep=sep)

        buf += "}\n"

        if fp is None:
            return buf
        else:
            with open(fp, "w") as output:
                output.write(buf)

    def generate(self, fp: str | None = None) -> str | None:
        """
        Generates dot code for the graph.

        If fp is None, returns dot code.
        """
        return self._generate(fp=fp)

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

    def __init__(self, name: str = "Digraph"):
        """
        Class for digraphs in the pygraphv library.

        Can generate dot code for the graph.
        """

        self.name = name
        self.nodes = []

    def generate(self, fp: str = None) -> str | None:
        return self._generate(fp=fp, sep="->", graph="digraph")