from typing import Iterable, List, Optional

from pygraphv.style import *
from pygraphv.utils import get_dot_repr

class Node:
    """
    Node in any graph class in pygraphv library.
    """
    def __init__(self, label: str = "", children: Optional[List["Node"]] = None, styles: Optional[List[NodeStyle]] = None):
        self.label = label
        self.children = children if children is not None else []
        self.styles = (styles if isinstance(styles, Iterable) else [styles]) if styles is not None else []

    def generate(self, generated: Optional[List[int]] = None, sep: str = "--") -> str:
        """
        Generates dot code of node.
        """
        buf = ""
        generated = generated if generated is not None else []
        generated.append(id(self))

        if self.label:
            buf += f"Node{id(self)} [label={get_dot_repr(self.label)}];\n"
        if self.styles:
            buf += f"Node{id(self)} [{Style.generate_attrs(self.styles)}];\n"

        for i in self.children:
            if isinstance(i, Edge):
                if id(i.node) not in generated:
                    buf += i.node.generate(generated=generated, sep=sep)
                buf += f"Node{id(self)} {sep} Node{id(i.node)} [label={get_dot_repr(i.label)};"
                if i.styles:
                    buf += Style.generate_attrs(i.styles)
                buf += "];\n"
            else:
                if id(i) not in generated:
                    buf += i.generate(generated=generated, sep=sep)
                buf += f"Node{id(self)} {sep} Node{id(i)};\n"

        return buf

    def __str__(self) -> str:
        return self.generate()

class Edge:
    """
    Edge between two nodes in any graph class in pygraphv library.
    """

    def __init__(self, node: Node, label: str = "", styles: Optional[List[EdgeStyle]] = None):
        self.node = node
        self.label = label
        self.styles = (styles if isinstance(styles, Iterable) else [styles]) if styles is not None else []