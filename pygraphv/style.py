from dataclasses import dataclass


class Style:
    ATTRIBUTES: list[str] = [
        "class_", "colorscheme", "style", "fontcolor", "fontname", "fontsize", "URL",
        "target", "nojustify"
    ]

    @staticmethod
    def generate_attrs(styles: list) -> str:
        buf = ""
        for i in styles:
            buf += i.generate()
        return buf

    def generate(self):
        buf = ""
        for i in self.ATTRIBUTES:
            if self.__getattribute__(i) is not None:
                buf += f"{i}={self.__getattribute__(i)};\n"
        return buf

@dataclass
class GraphStyle(Style):
    ATTRIBUTES = [
        "_background", "bb", "bgcolor", "center", "charset", "clusterrank", "comment",
        "compound", "concentrate", "Damping", "defaultdist", "dim", "dimen", 
        "diredgeconstraints", "diredgeconstraints", "dpi", "epsilon", "esep",
        "fontnames", "forcelabels", "gradientangle", "imagepath", "inputscale",
        "k", "label_scheme", "labeljust", "labelloc", "landscape", "layout",
        "layerlistsep", "layerselect", "layersep", "layers", "levels", "levelsgap",
        "lheight", "lp", "lwidth", "margin", "maxiter", "mclimit", "mindist",
        "mode", "model", "mosek", "nodesep", "normalize", "nslimit",
        "newrank", "notranslate", "nslimit1", "ordering", "orientation", "outputorder",
        "overlap", "overlap_scaling", "overlap_shrink", "pack", "packmode", "pad",
        "page", "pagedir", "quantum", "quadtree", "rankdir", "ranksep", "ratio",
        "remincross", "repulsiveforce", "resolution", "root", "rotate", "rotation",
        "searchsize", "scale", "sep", "showboxes", "size", "smoothing", "sortv",
        "splines", "start", "stylesheet", "target", "truecolor", "viewport", "voro_margin",
        "xdotversion", *Style.ATTRIBUTES
    ]

    _background : object | None = None
    bb : object | None = None
    bgcolor : object | None = None
    center : object | None = None
    charset : object | None = None
    clusterrank : object | None = None
    comment : object | None = None
    compound : object | None = None
    concentrate : object | None = None
    Damping : object | None = None
    defaultdist : object | None = None
    dim : object | None = None
    dimen : object | None = None
    diredgeconstraints : object | None = None
    diredgeconstraints : object | None = None
    dpi : object | None = None
    epsilon : object | None = None
    esep : object | None = None
    fontnames : object | None = None
    forcelabels : object | None = None
    gradientangle : object | None = None
    imagepath : object | None = None
    inputscale : object | None = None
    k : object | None = None
    label_scheme : object | None = None
    labeljust : object | None = None
    labelloc : object | None = None
    landscape : object | None = None
    layout : object | None = None
    layerlistsep : object | None = None
    layerselect : object | None = None
    layersep : object | None = None
    layers : object | None = None
    levels : object | None = None
    levelsgap : object | None = None
    lheight : object | None = None
    lp : object | None = None
    lwidth : object | None = None
    margin : object | None = None
    maxiter : object | None = None
    mclimit : object | None = None
    mindist : object | None = None
    mode : object | None = None
    model : object | None = None
    mosek : object | None = None
    nodesep : object | None = None
    normalize : object | None = None
    nslimit : object | None = None
    newrank : object | None = None
    notranslate : object | None = None
    nslimit1 : object | None = None
    ordering : object | None = None
    orientation : object | None = None
    outputorder : object | None = None
    overlap : object | None = None
    overlap_scaling : object | None = None
    overlap_shrink : object | None = None
    pack : object | None = None
    packmode : object | None = None
    pad : object | None = None
    page : object | None = None
    pagedir : object | None = None
    quantum : object | None = None
    quadtree : object | None = None
    rankdir : object | None = None
    ranksep : object | None = None
    ratio : object | None = None
    remincross : object | None = None
    repulsiveforce : object | None = None
    resolution : object | None = None
    root : object | None = None
    rotate : object | None = None
    rotation : object | None = None
    searchsize : object | None = None
    scale : object | None = None
    sep : object | None = None
    showboxes : object | None = None
    size : object | None = None
    smoothing : object | None = None
    sortv : object | None = None
    splines : object | None = None
    start : object | None = None
    stylesheet : object | None = None
    target : object | None = None
    truecolor : object | None = None
    viewport : object | None = None
    voro_margin : object | None = None
    xdotversion : object | None = None
    class_ : object | None = None
    colorscheme : object | None = None
    style : object | None = None
    fontcolor : object | None = None
    fontname : object | None = None
    fontsize : object | None = None
    URL : object | None = None
    target : object | None = None
    nojustify : object | None = None
    

@dataclass
class NodeStyle(Style):
    """
    Style class of Node in pygraphv library.
    """
    ATTRIBUTES = [
        "area", "shape", "style", "color", "fillcolor", "class_", "colorscheme",
        "comment", "distortion", "fixedsize", "gradientangle", "group", 
        "href", "id", "image", "imagescale", "imagepos", "labelloc", "layer", "ordering",
        "orientation", "penwidth", "peripheries", "pin", "pos", "rects", "regular", "root", "samplepoints",
        "shapefile", "showboxes", "sides", "skew", "sortv", "style", "tooltip", "vertices",
        "width", "xlabel", "xlp", "z", *Style.ATTRIBUTES,
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