from dataclasses import dataclass


class Style:
    ATTRIBUTES: list[str]

    def generate(self):
        buf = ""
        for i in self.ATTRIBUTES:
            if self.__getattribute__(i) is not None:
                buf += f"{i}={self.__getattribute__(i)};\n"
        return buf

@dataclass
class NodeStyle(Style):
    """
    Style class of Node in pygraphv library.
    """
    ATTRIBUTES = [
        "area", "shape", "style", "color", "fillcolor", "fontcolor", "fontsize", "fontname", 
        "class_", "colorscheme", "comment", "distortion", "fixedsize", "gradientangle", "group", 
        "href", "id", "image", "imagescale", "imagepos", "labelloc", "layer", "nojustify", "ordering",
        "orientation", "penwidth", "peripheries", "pin", "pos", "rects", "regular", "root", "samplepoints",
        "shapefile", "showboxes", "sides", "skew", "sortv", "style", "target", "tooltip", "URL", "vertices",
        "width", "xlabel", "xlp", "z",
    ]

    area: float | None = None
    shape: str | None = None
    style: str | None = None
    color: str | None = None
    fillcolor: str | None = None
    fontcolor: str | None = None
    fontsize: int | None = None
    fontname: str | None = None
    class_: str | None = None
    colorscheme: str | None = None
    comment: str | None = None
    distortion: float | None = None
    fixedsize: bool | None = None
    gradientangle: int | None = None
    group: str | None = None
    href: str | None = None
    id: str | None = None
    image: str | None = None
    imagescale: float | None = None
    imagepos: str | None = None
    labelloc: str | None = None
    layer: int | None = None
    nojustify: str | None = None
    ordering: str | None = None
    orientation: str | None = None
    penwidth: float | None = None
    peripheries: int | None = None
    pin: str | None = None
    pos: str | None = None
    rects: str | None = None
    regular: str | None = None
    root: str | None = None
    samplepoints: str | None = None
    shapefile: str | None = None
    showboxes: str | None = None
    sides: int | None = None
    skew: float | None = None
    sortv: str | None = None
    style: str | None = None
    target: str | None = None
    tooltip: str | None = None
    URL: str | None = None
    vertices: str | None = None
    width: float | None = None
    xlabel: str | None = None
    xlp: float | None = None
    z: int | None = None