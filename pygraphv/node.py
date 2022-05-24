class Node:
    """
    Node in any graph class in pygraphv library.
    """
    def __init__(self, label: str = "", children: list["Node"] = None):
        self.label = label
        self.children = children if children is not None else []

    def generate(self, generated: list[int] = None, sep: str = "--") -> str:
        """
        Generates dot code of node.
        """
        buf = ""
        generated = generated if generated is not None else []
        generated.append(id(self))

        if self.label:
            buf += f"Node{id(self)} [label=\"{repr(self.label)[1:-1]}\"];\n"

        for i in self.children:
            if id(i) not in generated:
                buf += i.generate(generated=generated, sep=sep)
            buf += f"Node{id(self)} {sep} Node{id(i)};\n"

        return buf

    def __str__(self) -> str:
        return self.generate()