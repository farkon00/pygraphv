from dataclasses import dataclass

@dataclass
class Style:
    ATTRIBUTES = [
        "class_", "colorscheme", "fontcolor", "fontname", "fontsize", "href", "id",
        "nojustify", "style", "target", "tooltip", "URL"
    ]

    class_: str | None = None
    colorscheme: str | None = None
    fontcolor: str | None = None
    fontname: str | None = None
    fontsize: float | None = None
    href: str | None = None
    id: str | None = None
    nojustify: bool | None = None
    style: str | None = None
    target: str | None = None
    tooltip: str | None = None
    URL: str | None = None

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
                buf += f"{i}={value if not isinstance(value, str) else f'{quote}{repr(value)[1:-1]}{quote}'};"
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

    _background: str | None = None
    bb: str | None = None
    bgcolor: str | None = None
    center: bool | None = None
    charset: str | None = None
    clusterrank: str | None = None
    comment: str | None = None
    compound: bool | None = None
    concentrate: bool | None = None
    Damping: float | None = None
    defaultdist: float | None = None
    dim: int | None = None
    dimen: int | None = None
    diredgeconstraints: str | None = None
    dpi: float | None = None
    epsilon: float | None = None
    esep: str | None = None
    fontnames: str | None = None
    fontpath: str | None = None
    forcelabels: bool | None = None
    gradientangle: int | None = None
    imagepath: str | None = None
    inputscale: float | None = None
    K: float | None = None
    label_scheme: int | None = None
    labeljust: str | None = None
    labelloc: str | None = None
    landscape: bool | None = None
    layerlistsep: str | None = None
    layers: str | None = None
    layerselect: str | None = None
    layersep: str | None = None
    layout: str | None = None
    levels: int | None = None
    levelsgap: float | None = None
    lheight: float | None = None
    lp: str | None = None
    lwidth: float | None = None
    margin: float | None = None
    maxiter: int | None = None
    mclimit: float | None = None
    mindist: float | None = None
    mode: str | None = None
    model: str | None = None
    mosek: bool | None = None
    newrank: bool | None = None
    nodesep: float | None = None
    normalize: float | None = None
    notranslate: bool | None = None
    nslimit: float | None = None
    nslimit1: float | None = None
    ordering: str | None = None
    orientation: float | None = None
    outputorder: str | None = None
    overlap: str | None = None
    overlap_scaling: float | None = None
    overlap_shrink: bool | None = None
    pack: bool | None = None
    packmode: str | None = None
    pad: float | None = None
    page: float | None = None
    pagedir: str | None = None
    quadtree: str | None = None
    quantum: float | None = None
    rankdir: str | None = None
    ranksep: float | None = None
    ratio: float | None = None
    remincross: bool | None = None
    repulsiveforce: float | None = None
    resolution: float | None = None
    root: str | None = None
    rotate: int | None = None
    rotation: float | None = None
    scale: float | None = None
    searchsize: int | None = None
    sep: str | None = None
    showboxes: int | None = None
    size: float | None = None
    smoothing: str | None = None
    sortv: int | None = None
    splines: bool | None = None
    start: str | None = None
    stylesheet: str | None = None
    truecolor: bool | None = None
    viewport: str | None = None
    voro_margin: float | None = None
    xdotversion: str | None = None

@dataclass    
class ClusterStyle(GraphStyle):
    ATTRIBUTES = [
        "area", "color", "fillcolor", "layer", "pencolor", "penwidth", "peripheries", 
        *GraphStyle.ATTRIBUTES
    ]

    area: float | None = None
    color: str | None = None
    fillcolor: str | None = None
    layer: str | None = None
    pencolor: str | None = None
    penwidth: float | None = None
    peripheries: int | None = None

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

    area: float | None = None
    color: str | None = None
    comment: str | None = None
    distortion: float | None = None
    fillcolor: str | None = None
    fixedsize: bool | None = None
    gradientangle: int | None = None
    group: str | None = None
    height: float | None = None
    image: str | None = None
    imagepos: str | None = None
    imagescale: bool | None = None
    labelloc: str | None = None
    layer: str | None = None
    margin: float | None = None
    ordering: str | None = None
    orientation: float | None = None
    penwidth: float | None = None
    peripheries: int | None = None
    pin: bool | None = None
    pos: str | None = None
    rects: str | None = None
    regular: bool | None = None
    root: str | None = None
    samplepoints: int | None = None
    shape: str | None = None
    shapefile: str | None = None
    showboxes: int | None = None
    sides: int | None = None
    skew: float | None = None
    sortv: int | None = None
    vertices: str | None = None
    width: float | None = None
    xlabel: str | None = None
    xlp: str | None = None
    z: float | None = None
