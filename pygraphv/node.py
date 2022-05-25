from dataclasses import dataclass
from typing import Iterable

from pygraphv.style import *

class Node:
    """
    Node in any graph class in pygraphv library.
    """
    def __init__(self, label: str = "", children: list["Node"] = None, styles: list[NodeStyle] | None = None):
        self.label = label
        self.children = children if children is not None else []
        self.styles = (styles if isinstance(styles, Iterable) else [styles]) if styles is not None else []

    def generate(self, generated: list[int] = None, sep: str = "--") -> str:
        """
        Generates dot code of node.
        """
        buf = ""
        generated = generated if generated is not None else []
        generated.append(id(self))

        if self.label:
            buf += f"Node{id(self)} [label=\"{repr(self.label)[1:-1]}\"];\n"
        if self.styles:
            buf += f"Node{id(self)} [{Style.generate_attrs(self.styles)}];\n"

        for i in self.children:
            if isinstance(i, Edge):
                if id(i.node) not in generated:
                    buf += i.node.generate(generated=generated, sep=sep)
                buf += f"Node{id(self)} {sep} Node{id(i.node)} [label=\"{repr(i.label)[1:-1]}\"];\n"
            else:
                if id(i) not in generated:
                    buf += i.generate(generated=generated, sep=sep)
                buf += f"Node{id(self)} {sep} Node{id(i)};\n"

        return buf

    def __str__(self) -> str:
        return self.generate()

@dataclass
class Edge:
    node: Node
    label: str = ""