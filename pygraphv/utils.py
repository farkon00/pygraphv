from .html import DotHTML

def get_dot_repr(value) -> str:
    if isinstance(value, str):
        return "\"" + repr(value)[1:-1] + "\""
    else:
        return str(value)