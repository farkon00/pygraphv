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
    
    def generate(self, fp: str = None): # TODO: make generate function
        """
        Generate dot code for the graph.
        Writes code to file if fp(file path) is provided.
        """
        buf = ""

        buf += f"graph {self.name}" + " {\n"
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