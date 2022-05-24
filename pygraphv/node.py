class Node:
    def __init__(self, label: str = "", children: list["Node"] = None):
        self.label = label
        self.children = children if children is not None else []

    def generate(self):
        buf = ""
        
        return buf