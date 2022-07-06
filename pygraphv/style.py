from dataclasses import dataclass
from typing import Optional

from pygraphv.utils import get_dot_repr

@dataclass
class Style:
    ATTRIBUTES = [
        "class_", "colorscheme", "fontcolor", "fontname", "fontsize", "href", "id",
        "nojustify", "style", "target", "tooltip", "URL"
    ]

    class_: Optional[str] = None
    colorscheme: Optional[str] = None
    fontcolor: Optional[str] = None
    fontname: Optional[str] = None
    fontsize: Optional[float] = None
    href: Optional[str] = None
    id: Optional[str] = None
    nojustify: Optional[bool] = None
    style: Optional[str] = None
    target: Optional[str] = None
    tooltip: Optional[str] = None
    URL: Optional[str] = None

    @staticmethod
    def generate_attrs(styles: list) -> str:
        buf = ""
        for i in styles:
            buf += i.generate()
        return buf

    def generate(self):
        buf = ""
        quote = "\""
        for i in self.ATTRIBUTES:
            if self.__getattribute__(i) is not None:
                value = self.__getattribute__(i)
                buf += f"{i}={get_dot_repr(value)};"
        return buf

@dataclass
class GraphStyle(Style):
    ATTRIBUTES = [
        "_background", "bb", "bgcolor", "center", "charset", "clusterrank", "comment",
        "compound", "concentrate", "Damping", "defaultdist", "dim", "dimen", 
        "diredgeconstraints", "dpi", "epsilon", "esep", "fontnames", "fontpath", 
        "forcelabels", "gradientangle", "imagepath", "inputscale", "K", "label_scheme", 
        "labeljust", "labelloc", "landscape", "layerlistsep", "layers", "layerselect", 
        "layersep", "layout", "levels", "levelsgap", "lheight", "lp", "lwidth", 
        "margin", "maxiter", "mclimit", "mindist", "mode", "model", "mosek", 
        "newrank", "nodesep", "normalize", "notranslate", "nslimit", "nslimit1", 
        "ordering", "orientation", "outputorder", "overlap", "overlap_scaling", 
        "overlap_shrink", "pack", "packmode", "pad", "page", "pagedir", "quadtree", 
        "quantum", "rankdir", "ranksep", "ratio", "remincross", "repulsiveforce", 
        "resolution", "root", "rotate", "rotation", "scale", "searchsize", "sep", 
        "showboxes", "size", "smoothing", "sortv", "splines", "start", "stylesheet", 
        "truecolor", "viewport", "voro_margin", "xdotversion", *Style.ATTRIBUTES
    ]

    _background: Optional[str] = None
    bb: Optional[str] = None
    bgcolor: Optional[str] = None
    center: Optional[bool] = None
    charset: Optional[str] = None
    clusterrank: Optional[str] = None
    comment: Optional[str] = None
    compound: Optional[bool] = None
    concentrate: Optional[bool] = None
    Damping: Optional[float] = None
    defaultdist: Optional[float] = None
    dim: Optional[int] = None
    dimen: Optional[int] = None
    diredgeconstraints: Optional[str] = None
    dpi: Optional[float] = None
    epsilon: Optional[float] = None
    esep: Optional[str] = None
    fontnames: Optional[str] = None
    fontpath: Optional[str] = None
    forcelabels: Optional[bool] = None
    gradientangle: Optional[int] = None
    imagepath: Optional[str] = None
    inputscale: Optional[float] = None
    K: Optional[float] = None
    label_scheme: Optional[int] = None
    labeljust: Optional[str] = None
    labelloc: Optional[str] = None
    landscape: Optional[bool] = None
    layerlistsep: Optional[str] = None
    layers: Optional[str] = None
    layerselect: Optional[str] = None
    layersep: Optional[str] = None
    layout: Optional[str] = None
    levels: Optional[int] = None
    levelsgap: Optional[float] = None
    lheight: Optional[float] = None
    lp: Optional[str] = None
    lwidth: Optional[float] = None
    margin: Optional[float] = None
    maxiter: Optional[int] = None
    mclimit: Optional[float] = None
    mindist: Optional[float] = None
    mode: Optional[str] = None
    model: Optional[str] = None
    mosek: Optional[bool] = None
    newrank: Optional[bool] = None
    nodesep: Optional[float] = None
    normalize: Optional[float] = None
    notranslate: Optional[bool] = None
    nslimit: Optional[float] = None
    nslimit1: Optional[float] = None
    ordering: Optional[str] = None
    orientation: Optional[float] = None
    outputorder: Optional[str] = None
    overlap: Optional[str] = None
    overlap_scaling: Optional[float] = None
    overlap_shrink: Optional[bool] = None
    pack: Optional[bool] = None
    packmode: Optional[str] = None
    pad: Optional[float] = None
    page: Optional[float] = None
    pagedir: Optional[str] = None
    quadtree: Optional[str] = None
    quantum: Optional[float] = None
    rankdir: Optional[str] = None
    ranksep: Optional[float] = None
    ratio: Optional[float] = None
    remincross: Optional[bool] = None
    repulsiveforce: Optional[float] = None
    resolution: Optional[float] = None
    root: Optional[str] = None
    rotate: Optional[int] = None
    rotation: Optional[float] = None
    scale: Optional[float] = None
    searchsize: Optional[int] = None
    sep: Optional[str] = None
    showboxes: Optional[int] = None
    size: Optional[float] = None
    smoothing: Optional[str] = None
    sortv: Optional[int] = None
    splines: Optional[bool] = None
    start: Optional[str] = None
    stylesheet: Optional[str] = None
    truecolor: Optional[bool] = None
    viewport: Optional[str] = None
    voro_margin: Optional[float] = None
    xdotversion: Optional[str] = None

@dataclass    
class ClusterStyle(GraphStyle):
    ATTRIBUTES = [
        "area", "color", "fillcolor", "layer", "pencolor", "penwidth", "peripheries", 
        *GraphStyle.ATTRIBUTES
    ]

    area: Optional[float] = None
    color: Optional[str] = None
    fillcolor: Optional[str] = None
    layer: Optional[str] = None
    pencolor: Optional[str] = None
    penwidth: Optional[float] = None
    peripheries: Optional[int] = None

@dataclass
class NodeStyle(Style):
    """
    Style class of Node in pygraphv library.
    """
    ATTRIBUTES = [
        "area", "color", "comment", "distortion", "fillcolor", "fixedsize", "gradientangle",
        "group", "height", "image", "imagepos", "imagescale", "labelloc", "layer", "margin", 
        "ordering", "orientation", "penwidth", "peripheries", "pin", "pos", "rects", "regular", 
        "root", "samplepoints", "shape", "shapefile", "showboxes", "sides", "skew", "sortv", 
        "vertices", "width", "xlabel", "xlp", "z"
    ]

    area: Optional[float] = None
    color: Optional[str] = None
    comment: Optional[str] = None
    distortion: Optional[float] = None
    fillcolor: Optional[str] = None
    fixedsize: Optional[bool] = None
    gradientangle: Optional[int] = None
    group: Optional[str] = None
    height: Optional[float] = None
    image: Optional[str] = None
    imagepos: Optional[str] = None
    imagescale: Optional[bool] = None
    labelloc: Optional[str] = None
    layer: Optional[str] = None
    margin: Optional[float] = None
    ordering: Optional[str] = None
    orientation: Optional[float] = None
    penwidth: Optional[float] = None
    peripheries: Optional[int] = None
    pin: Optional[bool] = None
    pos: Optional[str] = None
    rects: Optional[str] = None
    regular: Optional[bool] = None
    root: Optional[str] = None
    samplepoints: Optional[int] = None
    shape: Optional[str] = None
    shapefile: Optional[str] = None
    showboxes: Optional[int] = None
    sides: Optional[int] = None
    skew: Optional[float] = None
    sortv: Optional[int] = None
    vertices: Optional[str] = None
    width: Optional[float] = None
    xlabel: Optional[str] = None
    xlp: Optional[str] = None
    z: Optional[float] = None

@dataclass
class EdgeStyle(Style):
    """
    Style class of Edge in pygraphv library.
    """
    ATTRIBUTES = [
        "arrowhead", "arrowsize", "arrowtail", "color", "comment", "constraint", "decorate", "dir",
        "edgehref", "edgetarget", "edgetooltip", "edgeURL", "fillcolor", "head_lp", "headclip", 
        "headhref", "headlabel", "headport", "headtarget", "headtooltip", "headURL", "labelangle", 
        "labeldistance", "labelfloat", "labelfontcolor", "labelfontname", "labelfontsize", 
        "labelhref", "labeltarget", "labeltooltip", "labelURL", "layer", "len", "lhead", "lp", 
        "ltail", "minlen", "penwidth", "pos", "samehead", "sametail", "showboxes", "tail_lp", 
        "tailclip", "tailhref", "taillabel", "tailport", "tailtarget", "tailtooltip", "tailURL",
        "weight", "xlabel", "xlp", *Style.ATTRIBUTES
    ]

    arrowhead: Optional[str] = None
    arrowsize: Optional[float] = None
    arrowtail: Optional[str] = None
    color: Optional[str] = None
    comment: Optional[str] = None
    constraint: Optional[bool] = None
    decorate: Optional[bool] = None
    dir: Optional[str] = None
    edgehref: Optional[str] = None
    edgetarget: Optional[str] = None
    edgetooltip: Optional[str] = None
    edgeURL: Optional[str] = None
    fillcolor: Optional[str] = None
    head_lp: Optional[str] = None
    headclip: Optional[bool] = None
    headhref: Optional[str] = None
    headlabel: Optional[str] = None
    headport: Optional[str] = None
    headtarget: Optional[str] = None
    headtooltip: Optional[str] = None
    headURL: Optional[str] = None
    labelangle: Optional[float] = None
    labeldistance: Optional[float] = None
    labelfloat: Optional[bool] = None
    labelfontcolor: Optional[str] = None
    labelfontname: Optional[str] = None
    labelfontsize: Optional[float] = None
    labelhref: Optional[str] = None
    labeltarget: Optional[str] = None
    labeltooltip: Optional[str] = None
    labelURL: Optional[str] = None
    layer: Optional[str] = None
    len: Optional[float] = None
    lhead: Optional[str] = None
    lp: Optional[str] = None
    ltail: Optional[str] = None
    minlen: Optional[int] = None
    penwidth: Optional[float] = None
    pos: Optional[str] = None
    samehead: Optional[str] = None
    sametail: Optional[str] = None
    showboxes: Optional[int] = None
    tail_lp: Optional[str] = None
    tailclip: Optional[bool] = None
    tailhref: Optional[str] = None
    taillabel: Optional[str] = None
    tailport: Optional[str] = None
    tailtarget: Optional[str] = None
    tailtooltip: Optional[str] = None
    tailURL: Optional[str] = None
    weight: Optional[int] = None
    xlabel: Optional[str] = None
    xlp: Optional[str] = None
