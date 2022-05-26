class DotHTML:
    def __init__(self, value: str):
        self._value = value

    def __str__(self) -> str:
        return "<" + self._value + ">"
